#! /usr/bin/env python3
#coding: utf-8

import os
from PIL import Image
import numpy as np

class PreDataProcess(object):

    def __init__(self, FilePath, Folders):
        self.FilePath = FilePath
        self.Folders = Folders


    # 规范文件名称（加标签）
    def file_rename(self):
        folder_counter = 0
        for Folder in self.Folders:
            file_counter = 0
            folder = os.listdir(self.FilePath + Folder)
            for SubFile in folder:
                file_counter += 1
                os.rename(self.FilePath + Folder + '/' + SubFile, \
                        self.FilePath + Folder + '/' + str(folder_counter) + '_' + str(file_counter) + '.png')
            folder_counter += 1
        
    # 规范文件尺寸
    def file_resize(self, OutputFolder, Height, Width):
        for Folder in self.Folders:
            for SubFile in os.listdir(self.FilePath + Folder):
                FileOpened = Image.open(self.FilePath + Folder + '/' + SubFile)
                Img2RGB = FileOpened.convert('RGB')
                ResizedImg = Img2RGB.resize((Width, Height), Image.BILINEAR)
                ResizedImg.save(os.path.join(OutputFolder, os.path.basename(SubFile)))

    # 读取图片数据，返回numpy array数组
    def data2array(self, FileName, TrainFolder):
       Data = Image.open(TrainFolder + FileName)
       return np.array(Data)

    # 将数据整理成可以输入神经网络的格式
    def get_data_set(self, TrainFolder):
       X_train = []
       Y_train = []
       for SubFile in os.listdir(TrainFolder):
           # 添加图片数组到主list中
           x_train = self.data2array(FileName = SubFile, TrainFolder = TrainFolder)
           X_train.append(x_train)
           # 添加标签数组到主list中
           Y_train.append(int(SubFile.split('_')[0]))
       X_train = np.array(X_train)
       Y_train = np.array(Y_train)

       return (X_train, Y_train)
