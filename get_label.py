#!/usr/bin/env python3

import re
import numpy as np
from PIL import Image
import os
from label_image import LabelImage

label_image_folder = 'data/original/labels/'

class GetLabel:
    def __init__(self, file_folder, file_name):
        self.file_folder = file_folder
        self.file_name = file_name

    def getLabel(self):
        label_x_train = []
        count = 0
        for item in open(self.file_folder + self.file_name, 'r'):
            list_item = item.split(', ')
            len_list_item = len(list_item)
            # label_file_name
            label_file_name = list_item[0]
            # label_y_train
            if 2 < len_list_item:
                label_y_train = list_item[1]
            else:
                label_y_train = list_item[1].split('\n')[0]
            # label_x_train
            flag = 0      # prevent the second processing from covering the first result.
            col_start = 0 # start edge of labels
            col_end = 0   # end edge of labels
            if count < 1000:
                for i in range(2, len_list_item):
                    # mask the image
                    item_label = re.split(' *', ' '.join(list_item[2:]))
                    item_label_last = re.findall(r"\d+", item_label[-1])
                    item_label[-1] = item_label_last[-1]
                    sort_item_label = sorted(list(map(int, item_label)))
                    col_start = sort_item_label[2*(i-2)]
                    col_end = sort_item_label[2*(i-2)+1]
                    label_image = LabelImage(file_folder = label_image_folder, file_name = label_file_name, col_start = col_start, col_end = col_end, flag = flag)
                    label_image.labelImage()
                    flag = col_end # refresh flag
            else:
                label_image = LabelImage(file_folder = label_image_folder, file_name = label_file_name, col_start = col_start, col_end = col_end, flag = flag)
                label_image.labelImage()
            labeled_image = np.array(Image.open(label_image_folder + label_file_name))/127
            labeled_image = Image.fromarray(np.uint8(labeled_image))
            labeled_image.save(os.path.join(label_image_folder, os.path.basename(label_file_name)))
            count += 1
