# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:47:13 2022

@author: Hannah Gold
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from PIL import Image
from matplotlib import pyplot as plt

   



os.chdir('bayc')
print(os.getcwd())
count=0
for filename in os.listdir(os.getcwd()):
#     if count<1000000:
    count+=1
    f = os.path.join(os.getcwd(), filename)
    if f[-3::] not in {"png", "jpg"}: continue
    
    from PIL import Image
    image = Image.open(f)
    #img = cv.imread(f, cv.IMREAD_UNCHANGED)
    
    #######
    image_data = image.load()
    color=image_data[15,15]
    
    height,width = image.size
    for loop1 in range(height):
        for loop2 in range(width):
            if image_data[loop1,loop2]==color:
                image_data[loop1,loop2]=0,0,0,0
            
    
    import os.path as path

    two_up =  path.abspath(path.join(__file__ ,"../../"))
    #print(os.getcwd())
    image.save(r'C:\Users\Hannah Gold\Desktop\MIT\MIT2022_2023\Machine Learning 6.7900\6.7900FinalProject\bayc_no_bg/'+'pic'+str(count)+'.png')
    
           
            

            









