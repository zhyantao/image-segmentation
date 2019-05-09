#!/usr/bin/env python3

from model_v2 import *
from data import *
import numpy as np
import cv2
import os
import warnings
from PIL import Image

warnings.filterwarnings("ignore")
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def image_normalized(file_path):
    '''
    png, size: 64*720，grayscale
    :param dir_path: path to your images directory
    :return:
    '''
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img_shape = img.shape
    image_size = (img_shape[1],img_shape[0])
    img_standard = cv2.resize(img, (64, 720), interpolation=cv2.INTER_CUBIC)
    img_new = img_standard
    img_new = np.asarray([img_new / 255.])
    img_new = img_new[:, :, :, np.newaxis] # add 1 dimension
    return img_new,image_size


if __name__ == '__main__':

    #path to images which aring wating for predicting
    test_path = "data/test/"

    # save the predict images
    save_path = "data/predict/"

    dp = data_preprocess(test_path=test_path,save_path=save_path,flag_multi_class=True,num_classes=3)

    #load model
    model = load_model('weights/model_v2.hdf5')

    for name in os.listdir(test_path):
        image_path = os.path.join(test_path,name)
        x,img_size = image_normalized(image_path)
        results = model.predict(x)
        dp.saveResult([results[0]],img_size,name.split('.')[0])
        print(' Picture ' + name + ' predict complete.')
