from PIL import Image, ImageFont, ImageDraw
from operator import sub
import numpy as np
import matplotlib.pyplot as plt
import os


def stamp(path, serial_start):
    # Get the monotype font for the serials. Minimum of 12pt recommended
    font = ImageFont.truetype("PTMono-Regular.ttf", 12)

    # Exception handling
    try:
        if any(file.endswith('.jpg') for file in os.listdir(path)):
            os.mkdir(f"{path}/new")
        else:
            return "No .jpg files found in the folder"
    except FileNotFoundError:
        return "No folder"
    except FileExistsError:
        return "Folder called 'new' already exists"

    # Choosing the right starting number
    if serial_start == "":
        with open("serial.txt") as file:
            serial = int(file.read())
    else:
        serial = int(serial_start)

    # Stamp every jpg
    for file in sorted(os.listdir(path)):
        serial_str = str(serial).zfill(5)
        
        if file.endswith(".jpg"):
            # Import image
            img = Image.open(f"{path}/{file}")
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
            stamp_loc = tuple(map(sub, img.size, (39, 16)))
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
            final_img.save(f"{path}/new/{serial_str}.jpg")
        
            serial += 1

    # Update the serials.txt file to the latest serial number
    with open("serial.txt", mode="w") as file:
        file.write(str(serial))
    print("serial.txt updated")
    return "Serial images created in folder called 'new'"
