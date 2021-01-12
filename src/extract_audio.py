import os
import subprocess

"""
Audio processing class
"""

class audio_extract:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    """
    Take outputted video created from the super scaled images 
    and apply audio from the input using ffmpeg
    """
    def apply_audio_to_video(self):
        audio_apply_command =       ['ffmpeg', '-i', f'no_audio_{self.output_filename}', 
                                    '-i', f'{self.input_filename}', 
                                    '-c', 'copy', 
                                    '-map', '0:0', 
                                    '-map', '1:1', 
                                    '-shortest', f'{self.output_filename}']

        subprocess.call(audio_apply_command)