#!/usr/bin/env python3

from label_image import LabelImage
import re

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
            flag = 0 # 防止两次对一张图片编辑，第二次编辑对第一次的编辑覆盖
            col_start = 0 # 病变区域起始区
            col_end = 0   # 病变区域终止区
            if count < 1000:
                for i in range(2, len_list_item):
                    # mask the image
                    list_item_tmp = re.findall(r"\d+", list_item[i]) # 使用正则表达式去除\n https://zhidao.baidu.com/question/328905513600600605.html
                    col_start = int(list_item_tmp[0])
                    col_end = int(list_item_tmp[1])
                    label_image = LabelImage(file_folder = label_image_folder, file_name = label_file_name, col_start = col_start, col_end = col_end, flag = flag)
                    label_image.labelImage()
                    flag = col_end # 记录上一次修改末尾的数值，下一次不再修改前面的数值
            else:
                label_image = LabelImage(file_folder = label_image_folder, file_name = label_file_name, col_start = col_start, col_end = col_end, flag = flag)
                label_image.labelImage()
            count += 1
