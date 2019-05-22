#!/usr/bin/env python3

from PIL import Image
import numpy as np
import os

color_background = 0 # grayscale
color_label = 127
color_nlabel = 254
thresholds = 60

class LabelImage:
    def __init__(self, file_folder, file_name, col_start, col_end, flag):
        self.file_folder = file_folder
        self.file_name = file_name
        self.col_start = col_start # the edge of start labeling
        self.col_end = col_end     # the edge of end labeling
        self.flag = flag

    # change the input images into desired output images and then put them in the labels folder.
    def labelImage(self):
        image = Image.open(self.file_folder + self.file_name)
        image_array = np.array(image)
        image_array_height = image_array.shape[0]
        image_array_width = image_array.shape[1]
        for w in range(self.flag, image_array_width):
            for h in range(0, image_array_height):
                if w >= self.col_start-1 and w <= self.col_end-1 and int(self.file_name.split('.')[0]) <= 1000:
                    if image_array[h, w] < thresholds + 30:  # vulnerable plaques thresholds
                        image_array[h, w] = color_background # background
                    else:
                        image_array[h, w] = color_label      # is label
                else:
                    if image_array[h, w] < thresholds:       # unvulnerable plaques thresholds
                        image_array[h, w] = color_background # background
                    else:
                        image_array[h, w] = color_nlabel     # is NOT label
        label_image = Image.fromarray(np.uint8(image_array))
        # save labeled image
        label_image.save(os.path.join(self.file_folder, os.path.basename(self.file_name)))
        print('\r Processing picture {}'.format(self.file_name), end='')
        return label_image
