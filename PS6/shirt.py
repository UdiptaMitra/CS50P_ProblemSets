"""After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt.
No need to buy one online, but like to try one on virtually?
Implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size,
saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with
ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering,
overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:
if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py.No need to submit any photos
with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!

Note that you can determine a file’s extension with os.path.splitext, per docs.python.org/3/library/os.path.html#os.path.splitext.
Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
Note that the Pillow package comes with quite a few classes and methods, per pypi.org/project/Pillow. You might find its handbook and reference helpful to skim. You can install the package with:
pip install Pillow

And you can overlay that image on top of another (e.g., photo) with code like
photo.paste(shirt, shirt)
wherein the first shirt represents the image to overlay and the second shirt represents a “mask” indicating which pixels in photo to update.
"""

import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
before = sys.argv[1]
after = sys.argv[2]
_, path1 = os.path.splitext(before)
_, path2 = os.path.splitext(after)
if path1.lower() not in [".jpeg", ".jpg", ".png"]:
    sys.exit("not an image fileformat")
if path1.lower() != path2.lower():
    sys.exit("before after file paths not same")
try:
    with Image.open(before) as img:
        with Image.open("shirt.png") as shirt:
            size = shirt.size
            img = ImageOps.fit(img, size)
            img.save(before)
            img.paste(shirt, shirt)
            img.save(after)
except FileNotFoundError:
    sys.exit("Input does not exist")
