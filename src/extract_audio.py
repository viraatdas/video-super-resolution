import os
import ffmpeg

class audio_extract:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def extract_input_audio_and_apply(self):
        input_audio = ffmpeg.input(self.input_filename, f='mp3')
        output_video = ffmpeg.input(self.output_filename)

        ffmpeg.concat(output_video, input_audio, v=1, a=1).output(f"finished.mp4").run()
