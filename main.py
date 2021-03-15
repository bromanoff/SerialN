from PIL import Image, ImageFont, ImageDraw
from operator import sub
import numpy as np
import matplotlib.pyplot as plt

# file_loc = input("Please give a specific file location. Every picture in this directory will be processed: ")

# img = Image.open("test/scan_4800dpi.jpg")
img = Image.open("test/test_2.jpg")

font = ImageFont.truetype("CourierPrime-Regular.ttf", 10)

draw = ImageDraw.Draw(img)

serial = "0123456789"
stamp = tuple(map(sub, img.size, (200, 100)))

draw.text(stamp, serial, (255), font)

img.show()






