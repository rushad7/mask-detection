import os
import cv2

files = os.listdir(r'C:\Users\Rushad\Desktop\mask')

for i in range(len(files)):
    img = cv2.imread(files[i])
    img_flip = cv2.flip(img, 1)
    img_name = str(files[i]) + str(i*10) + ".jpg"
    cv2.imwrite(img_name, img_flip)

print("Data Augmentation Completed")
