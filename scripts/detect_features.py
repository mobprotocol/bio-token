import cv2
import dlib
import os
import sys

def main():
    '''
        view facial features of a given subject via dlib detector
        args:
            first_name
            last_name
    '''

    # path to targeted data
    data_path = './processed_data/{0}_{1}'.format(sys.argv[1], sys.argv[2])

    # make sure dete exists
    assert os.path.exists(data_path)

    # instnatiate dlib face detector
    detector = dlib.get_frontal_face_detector()

    # instantiate dlib facial feature finder
    predictor = dlib.shape_predictor('./dlib_shape_predictor.dat') # .dat is a pretrained model

    # iterate through data
    for image_name in os.listdir(data_path):

        # read image from disk
        image = cv2.imread('{0}/{1}'.format(data_path, image_name))

        # find faces with dlib
        faces = detector(image, 1)

        print(faces)

        # for (i, face) in enumerate(faces):
        #     shape = predictor(image, face)





if __name__ == '__main__':
    # make sure args are given
    assert len(sys.argv) == 3

    # start script
    main()
