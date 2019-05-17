#!/bin/sh

if [ -e data/original/images ]
then
	echo 'successfully make directory data/original/images'
else
	mkdir data/original/images
	echo 'successfully make directory data/original/images'
fi
if [ -e data/original/labels ]
then
	echo 'successfully make directory data/original/labels'
else
	mkdir data/original/labels
	echo 'successfully make directory data/original/labels'
fi
if [ -e data/predict ]
then
	echo 'successfully make directory data/predict'
else
	mkdir data/predict
	echo 'successfully make directory data/predict'
fi
if [ -e data/'test' ]
then
	echo 'successfully make directory data/test'
else
	mkdir data/'test'
	echo 'successfully make directory data/test'
fi
if [ -e data/train ]
then
	echo 'successfully make directory data/train'
else
	mkdir data/train
	echo 'successfully make directory data/train'
fi
if [ -e data/train_label ]
then
	echo 'successfully make directory data/train_label'
else
	mkdir data/train_label
	echo 'successfully make directory data/train_label'
fi
if [ -e data/val ]
then
	echo 'successfully make directory data/val'
else
	mkdir data/val
	echo 'successfully make directory data/val'
fi
if [ -e data/val_label ]
then
	echo 'successfully make directory data/val_label'
else
	mkdir data/val_label
	echo 'successfully make directory data/val_label'
fi
if [ -e log ]
then
	echo 'successfully make directory log'
else
	mkdir log
	echo 'successfully make directory log'
fi
if [ -e weights ]
then
	echo 'successfully make directory weights'
else
	mkdir weights
	echo 'successfully make directory weights'
fi
if [ -e TrainData.tar.gz ]
then
	tar zxf TrainData.tar.gz
	echo 'successfully extract file TrainData.tar.gz to TrainData'
else
	echo 'Cannot find file TrainData.tar.gz, please download it at https://pan.baidu.com/s/1WRdH2HjVpIi6cjRVHrhO8Q PASSWORD: msla'
fi
if [ -e TrainData/images ]
then
	cp TrainData/images/* data/original/images/ -f
	cp TrainData/images/* data/original/labels/ -f
	echo 'successfully put original data to folders'
	rm TrainData -rf
else
	echo 'May be you have not extract file TrainData.tar.gz, please extract it first.'
fi
