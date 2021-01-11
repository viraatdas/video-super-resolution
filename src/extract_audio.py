import os
import subprocess

class audio_extract:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def apply_audio_to_video(self):
        audio_apply_command =   f"""ffmpeg -i no_audio_{self.output_filename} 
                                    -i {self.input_filename} 
                                    -c copy -map 0:0 
                                    -map 1:1 
                                    -shortest {self.output_filename}""".replace('\n', ' ').replace('\t', '')

        subprocess.call(audio_apply_command)