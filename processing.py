import pandas as pd
import os
import numpy as np
import shutil

dataset = pd.read_csv('E:\\Project Dataset\\CompressedChestXRayPart\\max1800.csv')

file_names = np.array(dataset['Image Index'].values)
img_labels = np.array(dataset['Finding Labels'].values)


folders_to_be_created = np.unique(img_labels)
print(folders_to_be_created)

source = os.getcwd()


folders = folders_to_be_created.copy()
print(folders)


for new_path in folders_to_be_created:
    if not os.path.exists('E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s' %new_path):
        os.makedirs('E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s' %new_path)

        

for new_path in folders_to_be_created:
    if not os.path.exists('E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s' %new_path):
        os.makedirs('E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s' %new_path)

# 1. Cardiomegaly

for f in range(875):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(875, 1094):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 2. Hernia

for f in range(1094, 1095+87):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1095+87, 1205):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 3. Pneumonia 

for f in range(1205, 1205+257):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1205+257, 1527):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 4. Fibrosis

for f in range(1527, 1527+581):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(1527+581, 2254):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 5. Edema

for f in range(2254, 2254+502):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(2254+502, 2882):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 6. Emphysema

for f in range(2882, 2882+713):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(2882+713, 3774):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)

  
# 7. Pleural Thickening

for f in range(3774, 3774+900):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(3774+900, 4900):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 8. Consolidation 

for f in range(4900, 4900+1047):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(4900+1047, 6210):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 9. Pneumothorax

for f in range(6210, 6210+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(6210+1440, 8011):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 10. Mass

for f in range(8011, 8011+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(8011+1440, 9812):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
    

# 11. Nodule

for f in range(9812, 9812+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(9812+1440, 11613):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 12. Atelectasis

for f in range(11613, 11613+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(11613+1440, 13414):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 13. Effusion

for f in range(13414, 13414+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(13414+1440, 15215):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
  

# 14. Infiltration

for f in range(15215, 15215+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(15215+1440, 17016):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)


# 15. No Finding

for f in range(17016, 17016+1440):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\train\\%s\\" %current_label)
  

for f in range(17016+1440, 188818):
  current_img = file_names[f]
  current_label = img_labels[f]
  shutil.copy("E:\\Project Dataset\\CompressedChestXRayPart\\images_compressed\\%s" %current_img, "E:\\Project Dataset\\Chest-XRay-Dataset\\test\\%s\\" %current_label)
    
