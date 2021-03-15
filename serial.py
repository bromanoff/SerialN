from PIL import Image, ImageFont, ImageDraw
from operator import sub
import numpy as np
import matplotlib.pyplot as plt
import os

# Choose font for the serial number
font = ImageFont.truetype("PTMono-Regular.ttf", 12)

# Path to image dir
path = "/Users/roman/Documents/CodingProjects/100_Days_of_Code/day-81+_Portfolio_Projects/Image_SerialN/test/"


# Get the serial number
def get_serial(start):
    if start == "last":
        with open("serial.txt") as file:
            serial = file.read()
        return int(serial)
    else:
        serial = start
        return int(serial)


# Update the txt file to the latest serial number
def update_serial():
    update = str(serial)
    with open("serial.txt", mode="w") as file:
        file.write(update)
    print("serial.txt updated")

os.mkdir(f"{path}new")
serial = get_serial("1")
print(f"serial: {serial}")

for file in sorted(os.listdir(path)):
    serial_str = str(serial).zfill(5)
    
    if file.endswith(".jpg"):
        # Import image
        img = Image.open(path + file)
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
        stamp_loc = tuple(map(sub, img.size, (90, 50)))
        # Write white serial number on canvas
        draw.text(stamp_loc, serial_str, (255), font)
        # Convert canvas with serial back to array
        canvas_array = np.array(canvas_img)
        # Get the location of the serial number by value
        stamp_loc = np.where(canvas_array == 255)
        # Invert the image array
        img_array[stamp_loc] = 255 - img_array[stamp_loc]
        # Convert image array into pillow image object
        final_img = Image.fromarray(img_array)
        # Create new dir and saving image
        final_img.save(f"{path}new/{serial_str}.jpg")
    
        serial += 1

update_serial()
