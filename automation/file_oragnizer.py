

import os
import shutil

path = 'C:/test'
print("FILES FOUND:", os.listdir(path))
extensions = {item.split('.')[-1] for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))}

#create folder for each type 
for extension in extensions:
    if not os.path.exists(os.path.join(path , extension)):
        os.mkdir(os.path.join(path, extension))

#move files
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        file_extension = item.split('.')[-1]
        shutil.move(os.path.join(path , item), os.path.join(path, file_extension , item))