#!/bin/sh

# Demonstration, you can modify the file by your own.

# Trian data
rm data/train/*
cp data/original/images/[0-1][0-6]* data/train
rm data/train_label/*
cp data/original/labels/[0-1][0-6]* data/train_label

# Validation data
rm data/val/*
cp data/original/images/[0-1][7-8]* data/val
rm data/val_label/*
cp data/original/labels/[0-1][7-8]* data/val_label

# Test data
rm data/test/*
cp data/original/images/[0-1]90[0-9]* data/test

python file_rename.py
