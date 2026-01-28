import os
import shutil

path = "C:/test"
empty_folder = os.path.join(path, "empty_files")


if not os.path.exists(empty_folder):
    os.mkdir(empty_folder)

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        shutil.move(file_path, os.path.join(empty_folder, file))


      
    
