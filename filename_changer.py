import os
import pandas as pd
import numpy as np

directory = "bayc"

count = 0

old_to_new = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f == "bayc/hashes.csv": continue
    old_to_new.append([f[5:], "unicorn_"+str(count)+".png"])
    os.rename(f, "bayc/bayc_"+str(count)+".jpg")
    count += 1

A = np.array(old_to_new)
df = pd.DataFrame(A, columns=['old','new'])

df.to_csv("bayc/renaming_scheme.csv")