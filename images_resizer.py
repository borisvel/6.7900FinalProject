# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:46:19 2022

@author: Hannah Gold
"""



import os
import numpy as np
import cv2

#https://dev.to/stokry/remove-background-from-images-with-python-dkj
#directory = ["unicorns", "bayc"]
#entries = os.listdir('bayc_resize64')
#directory = ["bayc_resize64"]




# Reading an image in default mode
#src = cv2.imread("Qma1aZPn7iS1vxkfip6kjGjbA5EUPDaunsApJJ8mUt8pyT.png")
   

import cv2 as cv

import sys

os.chdir('bayc_no_bg')
print(os.getcwd())
count=0
for filename in os.listdir(os.getcwd()):
    if count<1000000:
        count+=1
        f = os.path.join(os.getcwd(), filename)
        if f[-3::] not in {"png", "jpg"}: continue
        
        
        img = cv.imread(f, cv.IMREAD_UNCHANGED)
        
        
       
        img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)
        import os.path as path

        two_up =  path.abspath(path.join(__file__ ,"../../"))
        #print(os.getcwd())
        cv.imwrite(r'C:\Users\Hannah Gold\Desktop\MIT\MIT2022_2023\Machine Learning 6.7900\6.7900FinalProject\bayc_no_bg_256/'+'pic'+str(count)+'.png', img)