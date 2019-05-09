#!/usr/bin/env python3

from get_label import GetLabel
from label_image import LabelImage
from add_color import addColor
import os

if __name__ == '__main__':

    get_label = GetLabel(file_folder = 'data/original/', file_name = 'label.txt')
    get_label.getLabel()

    for item in os.listdir('data/original/labels'):
        addColor('data/original/labels/', item)
        print(item)
