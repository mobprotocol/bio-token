import cv2
import dlib
import os
import sys
import numpy as np
from feature_detection import convert_rect, shape_to_np

def main():
    '''
        view facial features of a given subject via dlib detector
        https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
        args:
            first_name
            last_name
    '''

    # path to targeted data
    data_path = './processed_data/{0}_{1}'.format(sys.argv[1], sys.argv[2])

    # make sure data exists
    assert os.path.exists(data_path)

    # instnatiate dlib face detector
    detector = dlib.get_frontal_face_detector()

    # instantiate dlib facial feature finder
    predictor = dlib.shape_predictor('./dlib_shape_predictor.dat') # .dat is a pretrained model

    # iterate through data
    for image_name in os.listdir(data_path):
        print(image_name)

        # read image from disk
        image = cv2.imread('{0}/{1}'.format(data_path, image_name))

        # find faces with dlib
        faces = detector(image, 1)

        # iterate through all faces detected
        for (i, face) in enumerate(faces):

            # get landmarks from image
            raw_shape = predictor(image, face)

            # process landmark coordinates
            shape = shape_to_np(raw_shape)

            # convert frame
            (x, y, w, h) = convert_rect(face)

            # draw the bounding box on cv2 image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # draw landmarks on cv2 image
            for (x, y) in shape:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1),

        # display detected featues
        cv2.imshow('faces', image)
        cv2.waitKey(1)

    # kill display
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # make sure args are given
    assert len(sys.argv) == 3

    # start script
    main()
