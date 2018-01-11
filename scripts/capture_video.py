import numpy as np
import cv2
import time
import os

def main():

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

    # get name from user
    first_name = input('enter your first name: ')
    last_name = input('enter your last name: ')

    # video codec
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    # video writer instance
    out = cv2.VideoWriter('data/captured/raw_video/' + first_name + '_' + last_name + '.avi', fourcc, 20.0, (1280, 720))

    capture_duration = 10 # seconds

    #
    capture = cv2.VideoCapture(0)

    # capture video for 10 seconds
    start_time = time.time()
    while(time.time() - start_time < capture_duration):

        # catpure video frames
        ret, frame = capture.read()

        if ret==True:
            # turn frame to gray scale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # save frame
            out.write(frame)

            # display
            cv2.imshow('frame', gray)
            cv2.waitKey(1)
        else:
            break

    # end video capture
    out.release()
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
