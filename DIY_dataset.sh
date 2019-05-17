#!/bin/sh

# Demonstration, you can modify the file by your own.

# Trian data
if [ "`ls data/train/`" = "" ]
then
	echo 'Please run command `sh make_dataset.sh` first.'
else
	rm data/train/*
	cp data/original/images/[0-1][0-6]* data/train
	echo 'Copy tarin data complete.'
fi
if [ "`ls data/train_label/`" = ""  ]
then
	echo 'Please run command `sh make_dataset.sh` first.'
else
	rm data/train_label/*
	cp data/original/labels/[0-1][0-6]* data/train_label
	echo 'Copy tarin_label data complete.'
fi

# Validation data
if [ "`ls data/val/`" != "" ]
then
	rm data/val/*
	cp data/original/images/[0-1][7-8]* data/val
	echo 'Copy val data complete.'
else
	echo 'Please run command `sh make_dataset.sh` first.'
fi
if [ "`ls data/val_label/`" != "" ]
then
	rm data/val_label/*
	cp data/original/labels/[0-1][7-8]* data/val_label
	echo 'Copy val_label complete.'
else
	echo 'Please run command `sh make_dataset.sh` first.'
fi

# Test data
if [ "`ls data/test/`" != "" ]
then
	rm data/test/*
	cp data/original/images/[0-1]90[0-9]* data/test
	echo 'Copy test data complete.'
else
	echo 'Please run command `sh make_dataset.sh` first.'
fi

if [ -f file_rename.py ]
then
	python file_rename.py
	echo 'File rename complete.'
else
	echo 'Cannot find file file_rename.py.'
fi
