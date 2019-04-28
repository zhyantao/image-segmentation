#!/bin/sh

# Demonstration, you can modify the file by your own.

# Trian data
cp data/original/images/0[0-6]* data/train
cp data/original/labels/0[0-6]* data/train_label

# Validation data
cp data/original/images/0[7-8]* data/val
cp data/original/labels/0[7-8]* data/val_label

# Test data
cp data/original/images/09* data/test
