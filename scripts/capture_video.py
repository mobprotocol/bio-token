import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # catpure video frames
    ret, frame = cap.read()

    # manipulate frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display
    cv2.imshow('frame', gray)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
