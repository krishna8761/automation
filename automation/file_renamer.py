import os
import shutil
path = "C:/Users/ks392/OneDrive/Desktop/New folder (2)"
count = 1
for file in os.listdir(path) :
    old_path = os.path.join(path, file)

    if os.path.isfile(old_path):
        name = f"file_{count}.txt"
        new_path = os.path.join(path, name)

    os.rename(old_path , new_path)
    count += 1    