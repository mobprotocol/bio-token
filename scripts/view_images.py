import os
import cv2

example_file_path = './data/youtube_faces/aligned_images_DB/Aaron_Eckhart/0/'

for filename in os.listdir(example_file_path):
    image = cv2.imread(example_file_path + filename)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
