#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 08:31:40 2018

@author: esamuel
"""

import os
import glob

import cv2
import numpy as np

label_dir = "/home/victoria/pengyi/deepUNet/labels/"
target_dir = "/home/victoria/pengyi/deepUNet/targets/"
size_H = 512
size_W = 512

#那个记得要注意一下哈
#Numpy的图片格式: H x W x C
#Tensor的图片格式: C x H x W

for label in glob.glob(label_dir + "*.tif"):
    npy = label.replace(".tif", ".npy")
    index = cv2.imread(label)
    temp = np.zeros((size_H, size_W), dtype=np.uint8)
    temp[np.all(index == (255, 255, 255), axis=2)] = 0
    temp[np.all(index == (  0,   0, 255), axis=2)] = 1
    temp[np.all(index == (  0, 255, 255), axis=2)] = 2
    temp[np.all(index == (  0, 255,   0), axis=2)] = 3
    temp[np.all(index == (255, 255,   0), axis=2)] = 4
    temp[np.all(index == (255,   0,   0), axis=2)] = 5
    np.save(npy, temp)
    print("正在保存" + npy)
    
