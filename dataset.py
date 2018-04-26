#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:26:51 2018

@author: esamuel
"""

import os
import glob

#import cv2
import torch
import torchvision
from PIL import Image
#from skimage import io
import numpy as np
from torch.utils import data
from torchvision import transforms

transform_train = transforms.Compose([
    transforms.ToTensor()
])

class Isprs(data.Dataset):
    
    transform_train = transforms.Compose([
        transforms.ToTensor()
    ])

    def image_loader(path):
        #return cv2.imread(path)
        return Image.open(path)

    def numpy_loader(path):
        return np.load(path)
    
    def __init__(self, image_path="/home/victoria/pengyi/deepUNet/inputs/",
                 label_path="/home/victoria/pengyi/deepUNet/targets/",
                 transform=transform_train, input_loader=image_loader,
                 target_loader=numpy_loader):
        self.image_path = image_path
        self.label_path = label_path
        self.images = os.listdir(image_path) 
        self.labels = os.listdir(label_path)
        self.images.sort()
        self.labels.sort()
        self.transform = transform
        self.target_loader = target_loader
        self.input_loader = input_loader

    def __getitem__(self, index):
        inputs = self.input_loader(self.image_path + self.images[index])
        target = self.target_loader(self.label_path + self.labels[index])
        target = np.float32(target)
        if self.transform is not None:
            inputs = self.transform(inputs)
            #target = self.transform(target)
        target = torch.from_numpy(target)
        target = target.long()
        return inputs, target
    
    def __len__(self):
        return len(self.images)
