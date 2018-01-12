import os
import cv2
import codecs

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

                        # write image to disk
                        cv2.imwrite('{0}/{1}/{2}.jpg'.format(write_path, person, image_id), image)

if __name__ == '__main__':

    # start script
    main()
