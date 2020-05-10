import numpy as np
import cv2
import os

os.chdir(r"C:\Users\Rushad\Desktop\2")
img_list = os.listdir(r"C:\Users\Rushad\Desktop\2")
img_list = img_list[2:]
prototxt = r"C:\Users\Rushad\Desktop\prototxt.txt"
caffeModel = r"C:\Users\Rushad\Desktop\res10_300x300_ssd_iter_140000.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt, caffeModel)

for m in range(len(img_list)):
        image = cv2.imread(img_list[m])

        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()
        for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.5:
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")
                        roi = image[startY:endY,startX:endX]
                        Name = str(m) + ".jpg"
                        cv2.imwrite(Name, roi)
                        print("Image " + Name + " processed")
        print("Image Extraction complete")
