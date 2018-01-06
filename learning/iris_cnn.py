import os
from six.moves.urllib.request import urlopen
import csv

# data set urls
IRIS_TRAINING = 'iris_trining.csv'
IRIS_TRAINING_URL = 'http://download.tensorflow.org/data/iris_training.csv'
IRIS_TEST = 'iris_test.csv'
IRIS_TEST_URL = 'http://download.tensorflow.org/data/iris_test.csv'

def main():
    if not os.path.exists('./data/iris'):
        try:
            os.makedirs('./data/iris')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    if not os.path.exists('./data/iris/' + IRIS_TRAINING):
        raw = urlopen(IRIS_TRAINING_URL).read()
        try:
            with open('./data/iris/' + IRIS_TRAINING, 'wb') as f:
                f.write(raw)
        except IOError:
            print('could not write ' + IRIS_TRAINING + ' data to file')

    if not os.path.exists('./data/iris/' + IRIS_TEST):
        raw = urlopen(IRIS_TEST_URL).read()
        try:
            with open('./data/iris/' + IRIS_TEST, 'wb') as f:
                f.write(raw)
        except IOError:
            print('could not write ' + IRIS_TEST + ' data to file')
    
if __name__ == '__main__':
    main()
