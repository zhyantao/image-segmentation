#!/bin/sh

mkdir data/original/images
mkdir data/original/labels
mkdir data/predict
mkdir data/test
mkdir data/train
mkdir data/train_label
mkdir data/val
mkdir data/val_label
mkdir log
mkdir weights

tar zxf TrainData.tar.gz
rm TrainData.tar.gz
cp TrainData/images/* data/original/images/ -f
cp TrainData/labels/* data/original/labels/ -f
rm TrainData -rf
