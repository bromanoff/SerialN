from PIL import Image, ImageFont, ImageDraw
from operator import sub
import numpy as np
import matplotlib.pyplot as plt
import os


for file in os.listdir("./test"):
    print(file)
    # if file.endswith(".jpg"):
    #     img = Image.open(file)
    #     img.show()

# img = Image.open("./test/test_4.jpg")
# img.show()