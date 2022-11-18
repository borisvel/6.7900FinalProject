import os
import pandas as pd
import numpy as np
from PIL import Image



directory = ["unicorns", "bayc"]


def flatten(l):
    res = []
    for r, g, b in l:
        res.extend([r, g, b])
    return res


for directory in directory:
    images = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f == "bayc/hashes.csv" or f == "bayc/renaming_scheme.csv" \
                or f == "unicorns/data_rgb_format.csv" or f == "bayc/data_rgb_format.csv" or f == "unicorns/.ipynb_checkpoints": continue
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((200, 200))
        img_data = img.getdata()
        pixels = list(img_data)
        images.append(flatten(pixels))
    A = np.array(images)
    print(A.shape)
    df = pd.DataFrame(A, columns=[str(i) for i in range(A.shape[1])])
    df.to_csv(directory + "/data_rgb_format.csv")





