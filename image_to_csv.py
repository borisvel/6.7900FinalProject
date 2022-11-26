import os
import pandas as pd
import numpy as np
from PIL import Image
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

segmentor = SelfiSegmentation()


#directory = ["bayc", "unicorns"]
directory = ["bayc"]

def remove_background(img):
    background_color = img[4][4]
    size = img.shape[0]
    img_copy = np.copy(img)
    for i in range(size):
        for j in range(size):
            if np.linalg.norm(img_copy[i][j] - background_color, ord=2) <= 0.001:
                img_copy[i][j] = np.array([255, 255, 255])
    return img_copy


for directory in directory:
    images = []
    c = 0
    for filename in os.listdir(directory):
        if (c + 1)%1000 == 0: print(c + 1)
        f = os.path.join(directory, filename)
        if f[-3::] not in {"png", "jpg"}: continue
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA)
        #if directory == "bayc": img = remove_background(img)
        cv2.imwrite(directory + "_resize2/" + directory + "_" + str(c) + ".png", img)
        flat = img.flatten()
        images.append(flat)
        c += 1
    A = np.array(images)
    print(A.shape)
    df = pd.DataFrame(A, columns=[str(i) for i in range(A.shape[1])])
    df.to_csv(directory + "/data_rgb_format.csv")





