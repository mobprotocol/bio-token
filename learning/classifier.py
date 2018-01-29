import os
import tensorflow as tf
import cv2

data_path = './processed_data'

def get_data():
    data_set = []

    # iterate through data
    for person in os.listdir(data_path):
        if not person.startswith('.'):
            for image_name in os.listdir('{0}/{1}'.format(data_path, person)):
                if not image_name.startswith('.'):

                    # load image from disk
                    image = cv2.imread('{0}/{1}/{2}'.format(data_path, person, image_name))

                    # flatten image
                    pixel_array = image.flatten()

                    # add to label --> features to data list
                    data_set.append((person, pixel_array))

    # get total number of classes
    num_classes = len(os.listdir(data_path))
    print('number of classes: {0}'.format(num_classes))

    # get total number of images
    num_images = len(data_set)
    print('number of images: {0}'.format(num_images))

    return data_set

def split_data(data_set):


def main():
    data_set = get_data()
    train_data, test_data = split_data(data_set)


if __name__ == '__main__':
    # start script
    main()
