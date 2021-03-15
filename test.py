from PIL import Image, ImageFont, ImageDraw
from operator import sub
import numpy as np
import matplotlib.pyplot as plt


test_array = np.array(
                [[1, 255, 255, 255],
                 [255, 255, 255, 255],
                 [255, 255, 255, 255],
                 [255, 255, 255, 255]]
)

# Get the locaton of every 0 value
loc_array = np.where(test_array == 0)
print(loc_array)

test_array[loc_array] = 255

# Show images with matplotlib
plt.imshow(test_array, cmap = 'gray')
plt.show()

