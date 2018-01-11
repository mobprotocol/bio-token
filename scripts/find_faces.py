import numpy as np
import cv2

def find_faces(frame):
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

    # display detected features
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

    # end session
    cv2.destroyAllWindows()

def main():

if __name__ = '__main__':
    # given first and list name
    assert len(sys.argv) == 3

    # fetch video from file sytsem
    capture = cv2.VideoCapture('./data/captured/raw_video/{0}_{1}.avi'.format(sys.argv[0], sys.argv[1]))

    # iterate through video
    while(1):
            ret, frame = capture.read()
            if ret == True:
                find_faces(frame)
