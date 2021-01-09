"""
Module docstring
"""

__author__ = "Viraat Das"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from generate_upscale import upscale_video

def main(args):
    filename = args.filename
    remove_noise = args.remove_noise
    scale_factor = int(args.zoom)
    
    up_video = upscale_video(filename, remove_noise, scale_factor)
    up_video.upscale_images_from_video()

    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="Required positional argument")

    parser.add_argument("--zoom", default="2", help="Specifies scaling factor of video")

    parser.add_argument("--remove_noise", action="store_true", help="If specified, then will denoise the video")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)