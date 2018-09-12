import pandas as pd
import os
import numpy as np
import shutil

dataset = pd.read_csv('C:\\My Programs\\CompressedChestXRayPart\\max1800.csv')

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

# 1. Cardiomegaly

for f in range(875):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(875, 1094):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 2. Hernia

for f in range(1095, 1095+88):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1095+88, 1204):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 3. Pneumonia 

for f in range(1205, 1205+258):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1205+258, 1526):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 4. Fibrosis

for f in range(1527, 1527+582):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1527+582, 2253):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 5. Edema

for f in range(2254, 2254+503):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(2254+503, 2881):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 6. Emphysema

for f in range(2882, 2882+714):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(2882+714, 3773):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)

  
# 7. Pleural Thickening

for f in range(3774, 3774+901):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(3774+901, 4899):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 8. Consolidation 

for f in range(4900, 4900+1048):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(4900+1048, 6209):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 9. Pneumothorax

for f in range(6210, 6210+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(6210+1441, 8010):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 10. Mass

for f in range(8011, 8011+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(8011+1441, 9811):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
    

# 11. Nodule

for f in range(9812, 9812+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(9812+1441, 11612):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 12. Atelectasis

for f in range(11613, 11613+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(11613+1441, 13413):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 13. Effusion

for f in range(13414, 13414+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(13414+1441, 15214):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 14. Infiltration

for f in range(15215, 15215+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(15215+1441, 17015):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 15. No Finding

for f in range(17016, 17016+1441):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(17016+1441, 188817):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("c:\\My Programs\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "C:\\My Programs\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
    
