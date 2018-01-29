import cv2
import dlib
import numpy as np
import os
from feature_detection import convert_rect

def main():
    file_path = './processed_data/Emmit_Smith'

    # instnatiate dlib face detector
    detector = dlib.get_frontal_face_detector()

    # instantiate dlib facial feature finder
    predictor = dlib.shape_predictor('./dlib_shape_predictor.dat') # .dat is a pretrained model

    # iterate through all images
    for image_name in os.listdir(file_path):

        # read file from disk
        image = cv2.imread('{0}/{1}'.format(file_path, image_name))

        # find faces with pretrained dlib detector
        faces = detector(image, 1)

        # iterate though faces
        for face in faces:

            # convert dlib --> cv2 format
            (x, y, w, h) = convert_rect(face)
            print('w', w)
            print('h', h)

            # crop to face
            close_up = image[y:y+h, x:x+w]

            # display close-up image
            cv2.imshow('image', close_up)
            cv2.waitKey(1)



        # # get aligned images from dlib
        # aligned_images = dlib.get_face_chips(image, faces, size=320)

        # iterate through aligned images
        # for image in aligned_images:
        #     print(image)

if __name__ == '__main__':
    # start script
    main()
