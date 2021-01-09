from datetime import datetime
import cv2
import numpy as np
from PIL import Image
from ISR.models import RDN
import os

class upscale_video:
    def __init__(self, filename, remove_noise, zoom):
        self.filename = filename
        self.rdn = None
        if remove_noise:
            self.rdn = RDN(weights='noise-cancel')
        else:
            self.rdn = RDN(weights='psnr-large')
        
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

        self.dirname = f"upscaled_frames_{dt_string}"
        os.mkdir(self.dirname)

    def upscale_images_from_video(self):
        vidcap = cv2.VideoCapture(self.filename)
        success, lr_img = vidcap.read()
        count = 0
        while success:
            sr_img = self.rdn.predict(lr_img)
            img_filename = f"{count}.jpg"
            cv2.imwrite(os.path.join(self.dirname, img_filename), sr_img)   
            success, lr_img = vidcap.read()
            count += 1

