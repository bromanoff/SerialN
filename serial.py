from PIL import Image, ImageFont, ImageDraw
from operator import sub
import numpy as np
import matplotlib.pyplot as plt

# Choose font for the serial number
font = ImageFont.truetype("PTMono-Regular.ttf", 12)

# Get the serial number
serial = "04127"

# Import an image
img = Image.open("test/test_4.jpg")

# Create an array from image
img_array = np.array(img)

# Create a black canvas with image dimensions
canvas = np.zeros(img_array.shape)

# TODO create exception handling for 3darray/color images

# Create image from canvas
canvas_img = Image.fromarray(canvas) 

# Create a draw object that writes the serial number
draw = ImageDraw.Draw(canvas_img)
# Figure out the serial number location
serial_loc = tuple(map(sub, img.size, (90, 50)))
# Write white serial number on canvas
draw.text(serial_loc, serial, (255), font)

# Convert canvas with serial back to array
canvas_array = np.array(canvas_img)


# Get the location of the serial number by value
serial_loc = np.where(canvas_array == 255)


# Invert the image array
img_array[serial_loc] = 255 - img_array[serial_loc]

# Convert image array into pillow image object
final_img = Image.fromarray(img_array)


# Show image with pillow
final_img.show()

# Show images with matplotlib
# plt.imshow(canvas_img, cmap = 'gray')
# plt.show()
