#!/usr/bin/env python3

from PIL import Image
import numpy as np
import os

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
        #w_flag_label = []
        #w_flag_nlabel = []
        for w in range(0, image_array_width):
           # h_flag_label = 0
           # h_flag_nlabel = 0
            for h in range(0, image_array_height):
                if w >= self.col_start and w <= self.col_end:
                    if image_array[h, w] < 90:  # segmentation of vulnerable plaques and background thresholds
                        image_array[h, w] = 0   # background: Black
                    else:
                        image_array[h, w] = 255 # is label
                        #w_flag_label.append(w)
                        #if h > h_flag_label:
                        #    h_flag_label = h
                elif w >= self.flag:
                    if image_array[h, w] < 60:  # segmentation of vulnerable plaques and background thresholds
                        image_array[h, w] = 0   # background: Black
                    else:
                        image_array[h, w] = 128 # is NOT label
                        #w_flag_nlabel.append(w)
                        #if h > h_flag_nlabel:
                        #    h_flag_nlabel = h
            #image_array[0:h_flag_nlabel, w_flag_nlabel] = 128 # is NOT label
            #image_array[0:h_flag_label, w_flag_label] = 255   # is label
        label_image = Image.fromarray(np.uint8(image_array))
        # save labeled image
        label_image.save(os.path.join(self.file_folder, os.path.basename(self.file_name)))
        print(' Processing picture', self.file_name, '.')

