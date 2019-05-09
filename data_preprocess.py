#!/usr/bin/env python3

from get_label import GetLabel
from label_image import LabelImage
import os

if __name__ == '__main__':

    get_label = GetLabel(file_folder = 'data/original/', file_name = 'label.txt')
    get_label.getLabel()
    print()
