"""This program sorts downloaded file automatically."""


import os
import re
from pathlib import Path
import shutil

# (Temporarily) changing working directory
os.chdir('C:/Users/ezeki/Videos/Movies')

# Create the destination folder if it doens't exist
folder_path = Path("The Lincoln Lawyer Season 2")
folder_path.mkdir(exist_ok=True)

# Loop through the files in the current directory
for file in os.listdir():
    # Skip if the file is the folder itself
    if file == 'The Lincoln Lawyer Season 2':
        continue

    # Get the full path of the file
    file_path = Path(file)

    if file.startswith("The Lincoln Lawyer"):
        print(f"Moving: {file}")
        shutil.move(str(file_path), str(folder_path / file))

    # Process files that start with "tfpdl"
    if file.startswith("tfpdl"):
        name, ext = os.path.splitext(file)
        splitted = [s.strip() for s in name.split("-")]
        new_name = f"{splitted[1]}{ext}"

        # Apply regex replacements
        new_name = re.sub(r'tlnclwy\S*?', 'The Linoln Lawyer ', new_name)
        new_name = re.sub(r'20\S*?', 'S2_E', new_name)
        new_name = re.sub(r'72x\S*?', '_720p', new_name)

        # print(new_name)
        os.rename(file, new_name)
