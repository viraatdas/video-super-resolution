from datetime import datetime
import cv2
import numpy as np
from PIL import Image
from ISR.models import RDN
import os
from src.extract_audio import audio_extract

class upscale_video:
    def __init__(self, input_filename, remove_noise, zoom, output_filename):
        self.input_filename = input_filename
        self.rdn = None
        if remove_noise:
            self.rdn = RDN(weights='noise-cancel')
        else:
            self.rdn = RDN(weights='psnr-large')
        
        self.output_filename = output_filename
    
        self.vidcap = cv2.VideoCapture(self.input_filename)
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)
        self.fourcc = self.vidcap.get(cv2.CAP_PROP_FOURCC)
        width = int(self.vidcap.get(3))
        height = int(self.vidcap.get(4))
        self.frame_size = (width, height)
        self.out = cv2.VideoWriter(self.output_filename, -1, int(self.fps), self.frame_size)

    def upscale_images_from_video(self):
        ret, orig_img = self.vidcap.read()
        count = 0
        while ret:
            sr_img = self.rdn.predict(orig_img)
            self.out.write(sr_img)
            ret, orig_img = self.vidcap.read()
            count += 1
        self.out.release()

    def extract_and_apply_audio(self):
        apply_audio = audio_extract(self.input_filename, self.output_filename)
        apply_audio.extract_input_audio_and_apply()
