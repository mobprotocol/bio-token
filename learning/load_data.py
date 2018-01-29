import os
import tensorflow as tf
import random
import sys
import numpy as np
import threading

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
    shuffle_index = xrange(len(file_names))
    random.seed(12345)
    random.shuffle(shuffle_index)

    shuffled_file_names = [file_names[i] for i in shuffle_index]
    shuffled_labels = [labels[i] for i in shuffle_index]

    return shuffled_file_names, shuffled_labels

def process_data(file_names, labels):
    num_threads = 4
    ranges = []
    threads = []

    spacing = np.linspace(0, len(file_names), num_threads + 1).astype(np.int)

    for i in range(len(spacing) - 1):
        ranges.append([spacing[i], spacing[i] + 1])

    sys.stdout.flush()

    coord = tf.train.Coordinator()

    for thread_index in xrange(len(ranges)):
        args = (ranges, file_names, labels)
        t = threading.Thread(target=process_image_batch, args=args)
        t.start()
        threads.append(t)

    coord.join(threads)
    print('all threads are finished')
    sys.stdout.flush()
    
def process_image_batch(ranges, file_names, labels):
    print('thread running!')

def main():
    file_names, labels, num_labels = find_all_data('./processed_data/')
    # shuffled_file_names, shuffled_labels = shuffle_data(file_names, labels)
    process_data(file_names, labels)

if __name__ == '__main__':
    main()
