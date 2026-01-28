import os
import shutil
print('Enter the path of folder :')
path = input("what folder do you need to clean?: ")
empty_folder = os.path.join(path, "empty_files")


if not os.path.exists(empty_folder):
    os.mkdir(empty_folder)

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        shutil.move(file_path, os.path.join(empty_folder, file))


      
    
