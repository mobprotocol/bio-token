import tensorflow as tf
import numpy as np

class CNN():
    def __init__(self):
        self.mnist = tf.contrib.learn.datasets.load_dataset('mnist')
        self.train_data = self.mnist.train.images
        self.train_labels = np.asarray(self.mnist.train.labels, dtype=np.int32)
        self.eval_data = self.mnist.test.images
        self.eval_labels = np.asarray(self.mnist.test.labels, dtype=np.int32)

    def cnn_model_fn():
        '''
            Model for the cnn layers
        '''
        return true

cnn = CNN()
