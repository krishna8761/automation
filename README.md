 Python Empty File Cleaner

This is a simple Python automation script that moves empty files (size 0 bytes)
from a folder into a subfolder called `empty_files`.

 What it does
- Goes through all files in a specified folder.
- Checks each file’s size.
- If a file is empty (0 bytes), it moves it into `empty_files`.
- Handles duplicates safely.

 Concepts used
- `os` module for filesystem operations
- `shutil` module for moving files
- Looping and conditionals
- Path building using `os.path.join`

 How to use
1. Clone this repository:
link:
git clone https://github.com/krishna8761/automation
