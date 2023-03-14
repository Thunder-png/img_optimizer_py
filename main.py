# Image Optimizing
# pip install Pillow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import PIL
import glob
import os


def crop(x, y, z, q):
    # Croping
    im = PIL.Image.open("Image1.jpg")
    im = im.crop((x, y, z, q))


def resize(size, file):
    # Resizing
    im = PIL.Image.open(file)
    im = im.resize((size))
    im.save("Image_resize.jpg")


def flip():
    # Flipping
    im = PIL.Image.open("Image1.jpg")
    im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)


def rotate():
    # Rotating
    im = PIL.Image.open("Image1.jpg")
    im = im.rotate(360)


def compress():
    # Compressing
    im = PIL.Image.open("Image1.jpg")
    im.save("Image1.jpg", optimize=True, quality=90)


def blur():
    # Bluring
    im = PIL.Image.open("Image1.jpg")
    im = im.filter(PIL.ImageFilter.BLUR)


def sharp():
    # Sharpening
    im = PIL.Image.open("Image1.jpg")
    im = im.filter(PIL.ImageFilter.SHARPEN)


def bright():
    # Set Brightness
    im = PIL.Image.open("Image1.jpg")
    im = PIL.ImageEnhance.Brightness(im)
    im = im.enhance(1.5)


def contrast():
    # Set Contrast
    im = PIL.Image.open("Image1.jpg")
    im = PIL.ImageEnhance.Contrast(im)
    im = im.enhance(1.5)


def filter():
    # Adding Filters
    im = PIL.Image.open("Image1.jpg")
    im = PIL.ImageOps.grayscale(im)
    im = PIL.ImageOps.invert(im)
    im = PIL.ImageOps.posterize(im, 4)


def save():
    # Saving
    im.save("Image1.jpg")
