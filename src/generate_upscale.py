from datetime import datetime
import cv2
import numpy as np
from PIL import Image
from ISR.models import RDN
import os
import time
from moviepy.editor import ImageClip
from moviepy.editor import concatenate
from src.extract_audio import audio_extract

class upscale_video:
    def __init__(self, input_filename, remove_noise, zoom, output_filename):
        self.input_filename = input_filename
        self.rdn = None
        if remove_noise:
            self.rdn = RDN(weights='noise-cancel')
        else:
            self.rdn = RDN(weights='psnr-large')
        
        self.vidcap = cv2.VideoCapture(self.input_filename)
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)
    
        self.output_filename = output_filename
        self.output_video = None

    def upscale_images_from_video(self):
        video_clips = []
        ret, orig_img = self.vidcap.read()
        curr_time = time.time()
        while ret:
            sr_img = self.rdn.predict(orig_img)
            video_clips.append(ImageClip(sr_img).set_duration(1/self.fps))
            ret, orig_img = self.vidcap.read()
        print(f"Time it took to run ImageClip {time.time() - curr_time}")
        curr_time = time.time()
        self.output_video = concatenate(video_clips, method="chain")
        print(f"Time it took to concatenate {time.time() - curr_time}")

    def extract_audio_and_apply(self):
        apply_audio = audio_extract(self.input_filename, self.output_video , self.fps, self.output_filename)
        apply_audio.extract_input_audio_and_apply()
