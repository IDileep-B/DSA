# write a code for organizing file by type
import os
import shutil
def organize_files(folder):
if not os.path.exists(os.path.join(folder, "Images")):
os.mkdir(os.path.join(folder, "Images"))
if not os.path.exists(os.path.join(folder, "Documents")):
os.mkdir(os.path.join(folder, "Documents"))
for file in os.listdir(folder):
file_path = os.path.join(folder, file)
if os.path.isfile(file_path):
if file.endswith(".jpg"):
shutil.move(file_path, os.path.join(folder,

"Images", file))

elif file.endswith(".pdf"):
shutil.move(file_path, os.path.join(folder,

"Documents", file))
organize_files("Downloads")