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

# make sure ./data/captured/raw_video dir exists
if not os.path.exists('./data/captured/raw_video'):
    try:
        os.makedirs('./data/captured/raw_video')
    except OSError as e:
        raise

# get name
first_name = input('enter your first name: ')
last_name = input('enter your last name: ')

capture_duration = 10 # seconds
capture = cv2.VideoCapture(0)

# codec an videowriter
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('data/captured/raw_video/' + first_name + '_' + last_name + '.avi', fourcc, 20.0, (1280, 720))
video_counter = 0
# capture video for 10 seconds
start_time = time.time()
while(time.time() - start_time < capture_duration):
    # catpure video frames
    ret, frame = capture.read()
    h, w, channels = frame.shape
    if ret==True:
        # manipulate frames
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)

        # display
        cv2.imshow('frame', gray)
        cv2.waitKey(1)
    else:
        break

out.release()
capture.release()
cv2.destroyAllWindows()
