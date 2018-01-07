import numpy as np
import cv2
import time

capture_duration = 10 # seconds
capture = cv2.VideoCapture(0)

# codec an videowriter
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.Video

# capture video for 10 seconds
start_time = time.time()
while(time.time() - start_time < capture_duration):
    # catpure video frames
    ret, frame = capture.read()

    # manipulate frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display
    cv2.imshow('frame', gray)
    cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()
