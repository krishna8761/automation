import os
import shutil

path = "C:/test"

print("FILES FOUND:", os.listdir(path))

extensions = {
    item.split('.')[-1]
    for item in os.listdir(path)
    if os.path.isfile(os.path.join(path, item))
}

print("EXTENSIONS:", extensions)

for extension in extensions:
    folder_path = os.path.join(path, extension)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print("Created:", folder_path)

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        ext = item.split('.')[-1]
        dest = os.path.join(path, ext, item)
        print("Moving:", item, "->", dest)
        shutil.move(full_path, dest)

