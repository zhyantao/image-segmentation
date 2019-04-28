#!/usr/bin/env python3

from PIL import Image
import numpy as np
import os

class LabelImage:

    def __init__(self, file_folder, file_name, col_start, col_end, flag):
        self.file_folder = file_folder
        self.file_name = file_name
        self.col_start = col_start # 开始标记的区域
        self.col_end = col_end # 结束标记的区域
        self.flag = flag
    
    # 将图片转换为半黑半白的图片
    def labelImage(self):
        image = Image.open(self.file_folder + self.file_name)
        image_array = np.array(image)
        image_array_height = image_array.shape[0]
        image_array_width = image_array.shape[1]
        for i in range(0, image_array_width):
            if i >= self.flag: # 只对没有修改过的区域加白色
                image_array[:, i] = 255
            if i >= self.col_start and i <= self.col_end:
                image_array[:, i] = 0  # 黑色
        label_image = Image.fromarray(np.uint8(image_array))
        # 保存加标签后的图片
        label_image.save(os.path.join(self.file_folder, os.path.basename(self.file_name)))