# multithreaded support 
# https://github.com/opencv/opencv/blob/master/samples/python/video_threaded.py

"""
Module docstring
"""

__author__ = "Viraat Das"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from src.generate_upscale import upscale_video

def main(args):
    # parameters from arg
    filename = args.filename
    remove_noise = args.remove_noise
    scale_factor = int(args.zoom)
    output_filename = args.output_filename
    
    # create new frames apply Super Resolution
    up_video = upscale_video(filename, remove_noise, scale_factor, output_filename)
    up_video.upscale_images_from_video()
    up_video.extract_audio_and_apply()

    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="Required positional argument")

    parser.add_argument("--zoom", default="2", help="Specifies scaling factor of video")

    parser.add_argument("--remove_noise", action="store_true", help="If specified, then will denoise the video")

    parser.add_argument("--output_filename", default="ouput_video.mp4", help="Specify output filename")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)