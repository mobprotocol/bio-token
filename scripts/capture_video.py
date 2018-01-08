import numpy as np
import cv2
import time
import os

# make sure ./data/captured dir exists
if not os.path.exists('./data/captured'):
    try:
        os.makedirs('./data/captured')
    except OSError as e:
        raise

# get name
first_name = input('enter your first name: ')
last_name = input('enter your last name: ')

capture_duration = 10 # seconds
capture = cv2.VideoCapture(0)

# codec an videowriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('data/captured/' + first_name + '_' + last_name + '.avi',fourcc, 20.0, (640,480))

# capture video for 10 seconds
start_time = time.time()
while(time.time() - start_time < capture_duration):
    # catpure video frames
    ret, frame = capture.read()
    if ret==True:
        frame = cv2.flip(frame, 0)
        out.write(frame)

        # manipulate frames
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # display
        cv2.imshow('frame', gray)
        cv2.waitKey(1)
    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()
