#encoding:utf-8
#!/usr/bin/env python3

from model_v3 import  *
from data import *
import os
import keras
from keras.callbacks import TensorBoard
from keras.callbacks import EarlyStopping
import tensorflow as tf
import keras.backend.tensorflow_backend as K

config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
K.set_session(sess)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

if __name__ == '__main__':

    #path to images which are prepared to train a model
    train_path = "../data"
    image_folder = "train"
    label_folder = "train_label"
    valid_path =  "../data"
    valid_image_folder ="val"
    valid_label_folder = "val_label"
    log_filepath = '../log'
    flag_multi_class = True
    num_classes = 3
    dp = data_preprocess(train_path=train_path,image_folder=image_folder,label_folder=label_folder,
                         valid_path=valid_path,valid_image_folder=valid_image_folder,valid_label_folder=valid_label_folder,
                         flag_multi_class=flag_multi_class,
                         num_classes=num_classes)

    # train your own model
    train_data = dp.trainGenerator(batch_size=32)
    valid_data = dp.validLoad(batch_size=16)
    test_data = dp.testGenerator()
    model = unet(num_class=num_classes)

    tb_cb = TensorBoard(log_dir=log_filepath)
    model_checkpoint = keras.callbacks.ModelCheckpoint('../weights/model_v3.hdf5', monitor='val_loss',verbose=1,save_best_only=True)
    early_stopping_monitor = EarlyStopping(patience=3)
    history = model.fit_generator(train_data,
                                  steps_per_epoch=200,epochs=300,
                                  validation_steps=20,
                                  validation_data=valid_data,
                                  callbacks=[model_checkpoint,tb_cb,early_stopping_monitor])
