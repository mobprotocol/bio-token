import os
import tensorflow as tf
import random
import sys
import numpy as np

def find_all_data(data_path):
    '''
        finds file names and labels given a data path
        expects data_path --> [label1, label2,...]

        args: [string] path from project root to data
        returns: [tuple] (list, list, integer) file_names, labels, num_labels
    '''
    file_names = []
    num_labels = 0
    labels = []

    assert os.path.exists(data_path)

    for person in os.listdir(data_path):
        if not person.startswith('.'):
            num_labels += 1
            img_file_path = '{0}{1}'.format(data_path, person)
            for image in os.listdir(img_file_path):
                if not image.startswith('.'):
                    labels.extend(person)
                    file_names.extend('{0}/{1}'.format(img_file_path, image))

    return (file_names, labels, num_labels)

def shuffle_data(file_names, labels):
    '''
        shuffles incoming data
        args:
            file_names: [list] of image file paths
            labels: [list] of labels for images
        returns: [tuple] ([list], [list]) shuffled_file_names, shuffled_labels
    '''
    shuffle_index = range(len(file_names))
    random.seed(12345)
    random.shuffle(shuffle_index)

    shuffled_file_names = [file_names[i] for i in shuffle_index]
    shuffled_labels = [labels[i] for i in shuffle_index]

    return shuffled_file_names, shuffled_labels

def main():
    file_names, labels, num_labels = find_all_data('./processed_data/')
    shuffled_file_names, shuffled_labels = shuffle_data(file_names, labels)

if __name__ == '__main__':
    main()
