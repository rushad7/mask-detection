# mask-detection
This Python script is used to detect whether a people in the given image are wearing a mask or not.
The custom dataset was trained using Darknet.

### Usage for live detection:
python yolo-live-cv2.py --yolo yolo

### Usage for detection from images:
python custom_detector.py --image "/path/to/image" --config "/cfg/yolov3-custom.cfg" --weights "weights/yolov3-custom_final.weights" --names "class_names/voc.names"

### Misc Files
data_augmentation.py is a Python script to increase the sise of your dataset use data augmentation.  
rename.py is to rename the images and annotated .txt files to the same name according to the correct naming rules.  
test_train_split.py is to generate the test and train .txt files
