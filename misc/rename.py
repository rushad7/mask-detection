import os
import cv2
import hashlib

os.chdir(r"/home/rushad/Desktop/new_imgs")

img_list = []
for file in os.listdir("/home/rushad/Desktop/darknet/custom_data/images"):
    if file.endswith(".jpg"):
        img_list.append(os.path.join("/home/rushad/Desktop/darknet/custom_data/images", str(file)[:-4]))

txt_list = []
for file in os.listdir("/home/rushad/Desktop/darknet/custom_data/images"):
    if file.endswith(".txt"):
        txt_list.append(os.path.join("/home/rushad/Desktop/darknet/custom_data/images", str(file)[:-4]))

for m in range(len(img_list)):
	temp_new_name = hashlib.sha224(img_list[m]).hexdigest()
	temp_name_ext = str(temp_new_name) + str(".jpg") 
	temp_img = cv2.imread(str(img_list[m]) + ".jpg")
	cv2.imwrite(temp_name_ext, temp_img)

for n in range(len(txt_list)):
	temp_new_name = hashlib.sha224(img_list[n]).hexdigest()
	temp_name_ext = str(temp_new_name) + str(".txt")
	temp_file = open(str(img_list[n]) + ".txt", "r")
	temp_file_data = temp_file.read()
	temp_new_file = open(str(temp_name_ext), "w")
	temp_new_file.write(temp_file_data)
