import os
import cv2
import codecs
import dlib
from find_faces import find_faces

def main():
    '''
        processes youtube data into face close ups
        outputs to ./processed_data/first_last/
    '''

    # path to yt aligned data
    data_path = './data/youtube_faces/aligned_images_DB/'

    # path where processed data is written to
    write_path = './processed_data/'

    # make sure write_path exists
    if not os.path.exists(write_path):
        try:
            os.makedirs('./processed_data')
        except OSError as e:
            raise

    # iterate through all data
    for person in os.listdir(data_path):
        if not person.startswith('.'):

            # make sure directory exists for person
            person_path = '{0}/{1}'.format(write_path, person)
            if not os.path.exists(person_path):
                try:
                    os.makedirs(person_path)
                except OSError as e:
                    raise

            for image_set in os.listdir('{0}/{1}'.format(data_path, person)):
                if not image_set.startswith('.'):
                    for image_name in os.listdir('{0}/{1}/{2}'.format(data_path, person, image_set)):

                        # create cv2 image instance
                        image = cv2.imread('{0}/{1}/{2}/{3}'.format(data_path, person, image_set, image_name))

                        # generate unique id
                        image_id = codecs.encode(os.urandom(32), 'hex').decode()

                        # isolate face
                        close_up = find_faces(image)

                        # get height and width
                        h, w = close_up.shape

                        resized_image = cv2.resize(close_up, (100, 100), interpolation=cv2.INTER_CUBIC)
                        # f
                        cv2.imshow('image', resized_image)
                        cv2.waitKey(1)

                        # write image to disk
                        cv2.imwrite('{0}/{1}/{2}.jpg'.format(write_path, person, image_id), resized_image)

if __name__ == '__main__':

    # start script
    main()
