#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil

# Set the paths and filenames
image_folder = "trimmed"
label_file = "labels.txt"
output_folder = "new"

# Create output folders if they don't exist
even_folder = os.path.join(output_folder, "even")
odd_folder = os.path.join(output_folder, "odd")
os.makedirs(even_folder, exist_ok=True)
os.makedirs(odd_folder, exist_ok=True)

# Read the labels from the file
with open(label_file, 'r') as file:
    labels = file.read().splitlines()

# Iterate over the labels and move the corresponding images
for i, label in enumerate(labels):
    image_name = f"{i}.png"
    source_path = os.path.join(image_folder, image_name)
    if label == "EVEN":
        destination_path = os.path.join(even_folder, image_name)
    elif label == "ODD":
        destination_path = os.path.join(odd_folder, image_name)
    else:
        continue  # Skip if the label is neither EVEN nor ODD
    shutil.copyfile(source_path, destination_path)

print("Images separated and saved into even/odd folders.")

