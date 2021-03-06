import cv2
import dlib
import numpy
import numpy as np
import json

def detect_features(image):
    '''
        given an image finds landmark features
        args:
            cv2 image
        returns:
            flat list of landmark feature points
                63 * 2
    '''

    # instnatiate dlib face detector
    detector = dlib.get_frontal_face_detector()

    # instantiate dlib facial feature finder
    predictor = dlib.shape_predictor('./dlib_shape_predictor.dat') # .dat is a pretrained model

    # find faces with pretrained dlib detector
    faces = detector(image, 1)

    # list of feature sets
    features = []

    # iterate through detected faces
    for (i, face) in enumerate(faces):

        # get landmarks from image
        raw_shape = predictor(image, face)

        # process landmark coordinates
        shape = shape_to_np(raw_shape)

        features.append(shape.tolist())

    return features

def align_face(image, faces):
    '''
        aligns pose to forward position
        args:
            cv2 image
            list cv2 images (faces derived from base image)
        returns:
            list of cv2 images (aligned face close-ups)
    '''
    aligned_imags

def convert_rect(frame):
    '''
        converts from dlib to opencv fmt (x, y, w, h)
        args:
            frame: cv2 image
        returns:
            (x, y, w, h) tuple
    '''

    # conversions
    x = frame.left()
    y = frame.top()
    w = frame.right() - x
    h = frame.bottom() - y

    return (x, y, w, h)

def shape_to_np(shape):
    '''
        converts dlib object into np matrix
        arguments:
            shape: dlib feature predictor object
        returns:
            coords: np matrix 68 x 2
                68 landmark points
                2 (x, y) coordinates
    '''

    # initialize x, y coordinates
    coords = np.zeros((68, 2), dtype='int')

    # add all landmark features into coords
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords
