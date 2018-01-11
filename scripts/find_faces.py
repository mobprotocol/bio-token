import numpy as np
import cv2

def find_faces(frame):
    '''
        given an image with a face init
        returns image with frames around face and eyes

        args:
            frame: cv2 image instance
    '''
    
    # pre-trained opencv haar cascade algorithm \
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # turn frame to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect face/s in picture with haar cascade
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #draw rectangle around face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)]

        # draw rectangle around eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            if ret == True:
                find_faces(frame)

    return frame
