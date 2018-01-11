import os
import sys
import cv2

def main():
    '''
        allows you to view yt faces video
        args:
            first_name
            last_name
    '''

    # file path for yt data sets
    file_path = './data/youtube_faces/aligned_images_DB/{0}_{1}'.format(sys.argv[1], sys.argv[2])

    # make sure name is in data set
    assert os.path.exists(file_path)

    # iterate through images
    for image_set in os.listdir(file_path):
        for image_id in os.listdir('{0}/{1}'.format(file_path, image_set)):

            # create cv2 image
            image = cv2.imread('{0}/{1}/{2}'.format(file_path, image_set, image_id))

            # display image
            cv2.imshow('image', image)
            cv2.waitKey(1)

    # finish session
    cv2.destroyAllWindows()

if __name__ == '__main__':

    # make sure first and last name givem
    assert len(sys.argv) == 3

    # start script
    main()
