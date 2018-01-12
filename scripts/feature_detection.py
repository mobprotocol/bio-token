import cv2
import dlib
import numpy
import numpy as np

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
