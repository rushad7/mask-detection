# mask-detection
This Python script is used to detect whether a people in the given image are wearing a mask or not.
The custom dataset was trained using Darknet.

### Usage for detection from images:
Feel free to use python3 if required.
python2 yolo-live-cv2.py --yolo yolo

### Usage for detection from images:
python custom_detector.py --image "/path/to/image" --config "/cfg/yolov3-custom.cfg" --weights "weights/yolov3-custom_final.weights" --names "class_names/voc.names"
