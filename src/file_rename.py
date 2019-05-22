#encoding: utf-8
#!/usr/bin/env python3

import os

def file_rename(FilePath, Folders):
    for Folder in Folders:
        file_counter = 0
        folder = os.listdir(FilePath + Folder)
        for SubFile in folder:
            file_counter += 1
            os.rename(FilePath + Folder + '/' + SubFile, \
                    FilePath + Folder + '/' + str(file_counter) + '_' + SubFile.split('.')[0] + '.png')

if __name__ == '__main__':
    
    folders = ['train', 'train_label', 'val', 'val_label']
    file_rename('../data/', folders)
