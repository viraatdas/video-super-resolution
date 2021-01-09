#####
# import numpy as np
# from PIL import Image
# from ISR.models import RDN

# img = Image.open('data/input/test_images/section8-image.png')
# lr_img = np.array(img)

# rdn = RDN(weights='psnr-small')

# sr_img = rdn.predict(lr_img)
# im = Image.fromarray(sr_img)
# im.show()


####


"""
Module docstirng
"""

__author__ = "Viraat Das"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse


def main(args):

    print(args)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # ISR parameters
    # scaling factor --zoom
    # remove noise 

    parser.add_argument("--zoom", default="2")

    parser.add_argument("--remove_noise", action="store_true")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)