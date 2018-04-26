#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:12:51 2018

@author: esamuel
"""

import glob

from PIL import Image
import cv2

rootDir = "/home/esamuel/data/isprs/"
imageDir = "2_Ortho_RGB/"
labelDir = "5_Labels_for_participants/"
input_save = "inputs/"
label_save = "labels/"

aimX = 512
aimY = 512
orgX = 6000
orgY = 6000

totalNum = 0

def judge(num):
    if(num > 999):
        add = '00'
    elif(num > 99):
        add = '000'
    elif(num > 9):
        add = '0000'
    else:
        add = '00000'
    return add

def cutImage(image, label):
    global totalNum
    h = 0
    w = 0
    
    while(h < orgY):
        h += aimY
        if(h > orgY):
            h = orgY
        while(w < orgX):
            w += aimX
            if(w > orgX):
                w = orgX
            totalNum += 1
            add = judge(totalNum)
            
            tem = image[w-aimX:w, h-aimY:h]
            #tem = image.crop((w-aimX, h-aimY, w, h))
            path = rootDir + input_save + add + str(totalNum) + ".tif"
            cv2.imwrite(path, tem)
            #tem.save(path)
            
            tem = label[w-aimX:w, h-aimY:h]
            #tem = label.crop((w-aimX, h-aimY, w, h))
            path = rootDir + label_save + add + str(totalNum) + ".tif"
            cv2.imwrite(path, tem)
            #tem.save(path)
        w = 0

if __name__ == '__main__':
    for file in glob.glob(rootDir + labelDir + "*.tif"):
        label = cv2.imread(file)
        #label = Image.open(file)
        file = file.split('/')
        file = file[-1]
	file = file.rstrip("label.tif") + "RGB.tif"
        print("正在处理" + file)
        image = cv2.imread(rootDir + imageDir + file)
        #image = Image.open(rootDir + imageDir + file)
        cutImage(image, label)
