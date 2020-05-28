''' Usage :
    python test_train_split.py -d ~/mask-detection/annotations/
'''
import glob, os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True, help="Directory of dataset")
args = vars(ap.parse_args())

img_dir = str(args["dir"])
print(args["dir"])
percentage_test = 10;

file_train = open(r'~/mask-detection/train_test/train.txt', 'w')
file_test = open(r'~/mask-detection/train_test/test.txt', 'w')

counter = 1
index_test = round(100 / percentage_test)

for pathAndFilename in glob.iglob(os.path.join(img_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if int(counter) == int(index_test):
        counter = 1
        file_test = open(r'C:/Users/Rushad/Desktop/mask-detection/train_test/test.txt', 'a')
        file_test.write(img_dir + "/" + title + '.jpg' + "\n")
        file_test.close()
    else:
        file_train = open(r'C:/Users/Rushad/Desktop/mask-detection/train_test/train.txt', 'a')
        file_train.write(img_dir + "/" + title + '.jpg' + "\n")
        file_train.close()
        counter = counter + 1
