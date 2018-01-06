import os
from six.moves.urllib.request import urlopen
import csv
import numpy as np
import tensorflow as tf

# data set urls
IRIS_TRAINING = 'iris_trining.csv'
IRIS_TRAINING_URL = 'http://download.tensorflow.org/data/iris_training.csv'
IRIS_TEST = 'iris_test.csv'
IRIS_TEST_URL = 'http://download.tensorflow.org/data/iris_test.csv'

def fetch_iris_data():
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

def main():
    # write data to disk
    fetch_iris_data()

    # loada datasets
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename = './data/iris/' + IRIS_TRAINING,
        target_dtype=np.int,
        features_dtype=np.float32)

    # check data
    feature_columns = [tf.feature_column.numeric_column('x', shape=[4])]

    # build 3 layer dnn, with 10,20,10, units
    classifier = tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[10, 20, 10],
        n_classes=3,
        model_dir='/tmp/iris_model')

    # define the training inputs
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={'x': np.array(training_set.data)},
        y=np.array(training_set.target),
        num_epochs=None,
        shuffle=True)

    # train model
    classifier.train(input_fn=train_input_fn, steps=1000)

if __name__ == '__main__':
    main()
