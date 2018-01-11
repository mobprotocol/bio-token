import sys
import cv2
import os
from find_faces import find_faces

def main():
    '''
        processes video down into face close-up frames
        writes to ./process_data/first_last/___.jpg
        cli args:
            first_name,
            last_name
    '''

    # make sure ./data/processed_data directory exists
    if not os.path.exists('./processed_data'):
        try:
            os.makedirs('./processed_data')
        except OSError as e:
            raise

    # data write file path
    file_path = './processed_data/{0}_{1}'.format(sys.argv[1], sys.argv[2])

    # make sure ./data/processed_data/first_last exists
    if not os.path.exists(file_path):
        try:
            os.makedirs(file_path)
        except OSError as e:
            raise

    # fetch video from file system
    capture = cv2.VideoCapture('./data/captured/raw_video/{0}_{1}.avi'.format(sys.argv[1], sys.argv[2]))

    # iterate through video
    while(True):

        # get frame of video
        ret, frame = capture.read()

        if ret == True:
            # find face using util fn
            face_image = find_faces(frame)

            # random 16 byte id
            image_id = os.urandom(16)

            # write image to disk
            cv2.imwrite('{0}/{1}.jpg'.format(file_path, image_id), face_image)

        # finish when video is done
        else:
            break

    # release video capture
    capture.release()

if __name__ == '__main__':
    # make sure we have first and last name
    assert len(sys.argv) == 3

    # start script
    main()
