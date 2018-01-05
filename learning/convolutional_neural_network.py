import tensorflow as tf
import numpy as np

class CNN():
    def __init__(self):
        self.mnist = tf.contrib.learn.datasets.load_dataset('mnist')
        self.train_data = self.mnist.train.images
        self.train_labels = np.asarray(self.mnist.train.labels, dtype=np.int32)
        self.eval_data = self.mnist.test.images
        self.eval_labels = np.asarray(self.mnist.test.labels, dtype=np.int32)
        self.tensors_to_log = {'probabilities': 'softmax_tensor'}
        self.mnist_classifier = tf.estimator.Esimator(
            model_fn=self.cnn_model_fn,
            model_dir='/tmp/mnist_convnet_model')
        self.logging_hook = tf.train.LoggingTensorHook(
            tensors=self.tensors_to_log,
            every_n_iter=50)

    def train(self):
        self.train_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={'x': self.train_data},
            y=train_labels,
            batch_size=100,
            num_epochs=None,
            shuffle=True)
        self.mnist_classifier.train(
            input_fn=self.train_input_fn,
            steps=2000,
            hooks=[logging_hook])

    def cnn_model_fn():
        '''
            Model for the cnn layers
        '''
        return true

cnn = CNN()
