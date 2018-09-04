import pandas as pd
import os
import numpy as np
import shutil

dataset = pd.read_csv('C:\\My Programs\\CompressedChestXRayPart\\4177_single_diseases.csv')
file_names = np.array(dataset['Image Index'].values)
img_labels = np.array(dataset['Finding Labels'].values)


folders_to_be_created = np.unique(img_labels)
print(folders_to_be_created)

source = os.getcwd()


folders = folders_to_be_created.copy()
print(folders)


for new_path in folders_to_be_created:
    if not os.path.exists('C:\\My Programs\\Chest-XRay-Dataset\\train\\%s' %new_path):
        os.makedirs('C:\\My Programs\\Chest-XRay-Dataset\\train\\%s' %new_path)

        

for new_path in folders_to_be_created:
    if not os.path.exists('C:\\My Programs\\Chest-XRay-Dataset\\test\\%s' %new_path):
        os.makedirs('C:\\My Programs\\Chest-XRay-Dataset\\test\\%s' %new_path)


for f in range(3340):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(3340, 4177):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  