import os
import cv2
import numpy as np

capture = cv2.VideoCapture('./data/captured/sean_pollock.avi')

ret, frame = capture.read()
print(ret)
print(frame)
r, h, c, w = 250, 90, 400, 125
track_window = (c, r, w, h)

roi = frame[r: r+h, c: c+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# setup termination criteria
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while(1):
    ret, frame = capture.read()
    print(ret)
    print(frame)
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBlackProject([hsv], [0], roi_hist, [0,180], 1)

        # apply meanshift to get new location
        rest, track_window = cv2.meanShift(dst, track_window, term_criteria)

        # draw fram on image
        x, y, w, h = track_window
        img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        cv2.imshow('img2', img2)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite('./data/captured/sean_pollock/' + chr(k)    + '.jpg',img2)

cv2.destroyAllWindows()
capture.release()
