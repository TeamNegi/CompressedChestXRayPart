import pandas as pd
import os
import numpy as np
import shutil

# dataset = pd.read_csv('C:\\My Programs\\CompressedChestXRayPart\\4177_single_diseases.csv')
dataset = pd.read_csv('C:\\My Programs\\CompressedChestXRayPart\\balanced_data.csv')
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


for f in range(89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(89, 113):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

for f in range(113, 113+88):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(113+88, 222):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

for f in range(223, 312):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(312, 333):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  


for f in range(334, 423):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(423, 444):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  


for f in range(445, 445+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(445+89, 555):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  


for f in range(556, 556+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(556+89, 666):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  



for f in range(667, 667+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(667+89, 777):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
 

for f in range(778, 778+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(778+89, 888):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)



for f in range(889, 889+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(889+89, 999):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)



for f in range(1000, 1000+88):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1000+88, 1110):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
    


for f in range(1111, 1111+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1111+89, 1221):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  



for f in range(1221, 1221+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1221+89, 1332):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  



for f in range(1333, 1333+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1333+89, 1443):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  



for f in range(1444, 1444+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1444+89, 1554):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)




for f in range(1555, 1555+89):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1555+89, 1665):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
    