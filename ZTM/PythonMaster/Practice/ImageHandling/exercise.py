from PIL import Image
import os
import sys

# Grab First and second Argument
root_folder = os.path.abspath(os.getcwd())
loc_folder = sys.argv[1]
new_folder = sys.argv[2]

# Check is new/ exist
if not os.path.exists(new_folder):
    os.mkdir(new_folder)

file_list = os.listdir(loc_folder)
print(file_list)
for file in file_list:
    img = Image.open(f"./{loc_folder}{file}")
    #name = file[:-4]
    name = os.path.splitext(file)[0]
    img.save(f"{new_folder}{name}.png","png")

print("Files Converted")