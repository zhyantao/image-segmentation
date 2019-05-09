#!/usr/bin/env python3

from PIL import Image
import numpy as np
import os

# add a new color
def addColor(file_folder, file_name):
    image = Image.open(file_folder + file_name)
    image_array = np.array(image)
    image_array_height = image_array.shape[0]
    image_array_width = image_array.shape[1]
    w_flag_pipe = []
    for h in range(0, image_array_height):
        for w in range(0, image_array_width):
            if image_array[h, w] == 0 and h == 0:
                w_flag_pipe.append(w)
    image_array[0:image_array_height, w_flag_pipe] = 150
    label_image = Image.fromarray(np.uint8(image_array))

    # save labeled image
    label_image.save(os.path.join(file_folder, os.path.basename(file_name)))
