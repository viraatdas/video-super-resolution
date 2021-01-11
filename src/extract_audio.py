import os
import ffmpeg

class audio_extract:
    def __init__(self, input_filename, video, fps, output_filename):
        self.input_filename = input_filename
        self.video = video
        self.output_filename = output_filename
        self.fps = fps

    def extract_input_audio_and_apply(self):
        input_video_audio = AudioFileClip(self.input_filename)
        self.video.set_audio(input_video_audio)
        self.video.write_videofile(self.output_filename, fps=self.fps)