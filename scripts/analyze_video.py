import sys
import cv2
from find_faces import find_faces

def main():
    '''
        allows you to view face and eye detection of .avi video
        python3 ./scripts/analyze_video.py sean pollock
        cli args:
            first_name
            last_name
    '''

    # fetch video from file system
    capture = cv2.VideoCapture('./data/captured/raw_video/{0}_{1}.avi'.format(sys.argv[1], sys.argv[2]))

    # iterate through video
    while(True):

        # get frame from video
        ret, frame = capture.read()

        if ret == True:
            # find face usint util fn
            face_image = find_faces(frame)

            # display detectd features
            cv2.imshow('face_image', face_image)
            cv2.waitKey(1)

        # break when video is done
        else:
            break

    # release video
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # make sure we have first and last name
    assert len(sys.argv) == 3

    # start script
    main()
