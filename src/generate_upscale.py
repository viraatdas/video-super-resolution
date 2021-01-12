from datetime import datetime
import os

import cv2
from ISR.models import RDN
import subprocess

from src.extract_audio import audio_extract

"""
Video processing class
"""

class upscale_video:
    def __init__(self, input_filename, remove_noise, zoom, output_filename):
        self.input_filename = input_filename
        self.rdn = None

        # TODO add GAN support https://idealo.github.io/image-super-resolution/#gans-model
        if remove_noise:
            self.rdn = RDN(weights='noise-cancel')
        else:
            self.rdn = RDN(weights='psnr-large')
        
        self.output_filename = output_filename
        
        # create a unique dir name to save the updated frames
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        self.dirname = f"upscaled_frames_{dt_string}"
        os.makedirs(self.dirname)

        self.vidcap = cv2.VideoCapture(self.input_filename)
    
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)

    """
    Go frame by frame and save the scaled up images into the self.dirname
    """
    def upscale_images_from_video(self):
        ret, orig_img = self.vidcap.read()
        count = 0
        while ret:
            sr_img = self.rdn.predict(orig_img)
            img_filename = f"{count}.jpg"
            cv2.imwrite(os.path.join(self.dirname, img_filename), sr_img) 
            ret, orig_img = self.vidcap.read()
            count += 1

    """
    Use scaled up images and create video with no audio based off it
    """
    def combine_img_dir_into_video(self):
        video_ffmpeg_script = f"ffmpeg -framerate {int(self.fps)} -i {self.dirname}/%d.jpg no_audio_{self.output_filename}"
        subprocess.call(video_ffmpeg_script, shell=True)

    """
    Add audio to the super scaled video
    """
    def extract_and_apply_audio(self):
        apply_audio = audio_extract(self.input_filename, self.output_filename)
        apply_audio.apply_audio_to_video()
