import os
import sys
import cv2

def view_image_set():
    file_path = './data/youtube_faces/{0}_images_DB/{1}'.format(sys.argv[1], sys.argv[2])
    for image_set in os.listdir(example_file_path):
        print(image_set)
        image_path = file_path + '/' + image_set + '/'
        for imagename in os.listdir(image_path):
            image = cv2.imread(image_path + imagename)
            cv2.imshow("Image1", image)
            cv2.waitKey(100)
            cv2.destroyAllWindows()

assert len(sys.argv) == 3
assert sys.argv[1] == 'aligned' or 'frame'

view_image_set()
