import os
import tensorflow as tf

def find_all_data(data_path):
    '''

    '''
    file_names = []
    labels = []

    for person in os.listdir(data_path):
        if not person.startswith('.'):
            labels.extend(person)
            img_file_path = '{0}{1}'.format(data_path, person)
            for image in os.listdir(img_file_path):
                if not image.startswith('.'):
                    file_names.extend('{0}/{1}'.format(img_file_path, image))

    return (file_names, labels)

def shuffle_data(file_names):


def main():
    file_names, labels = find_all_data('./processed_data/')
    shuffled_data = shuffle_data(file_names)

if __name__ == '__main__':
    assert os.path.exists(data_path)
    main()
