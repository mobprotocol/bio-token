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
        '''
            training process
        '''
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
            model for the cnn layers
        '''
        #### INPUT LAYER
        self.input_layer = tf.reshape(features['x'], [-1, 28, 28, 1])

        #### CONVULUTIONAL LAYER 1
        self.conv1 = tf.layers.conv2d(
            inputs=self.input_layer,
            filters=32,
            kernel_size=[5,5],
            padding='same',
            activation=tf.nn.relu)

        #### POOLING LAYER 1
        self.pool1 = tf.layers.max_pooling2d(
            inputs=self.conv1,
            pool_size=[2, 2],
            strides=2)

        ### CONVULUTIONAL LAYER 2
        self.conv2 = tf.layers.conv2d(
            inputs=self.pool1,
            filters=64,
            padding='same',
            activation=tf.nn.relu)

        ### POOLING LAYER 2
        self.pool2 = tf.layers.max_pooling2d(
            inputs=self.conv2,
            pool_size=[2, 2],
            strides=2)

        ### DENSE LAYER
        self.pool2_flat = tf.reshape(
            pool2,
            [-1, 7 * 7 * 64])
        self.dense = tf.layers.dense(
            inputs=self.pool2_flat,
            units=1024,
            activation=tf.nn.relu)
        self.dropout = tf.layers.dropout(
            inputs=dense,
            rate=0.4,
            training=self.mode == tf.estimator.ModeKeyes.TRAIN)

        ### LOGITS LAYER
        self.logits = tf.layers.dense(
            inputs=self.dropout,
            units=10)

    def generate_predictions(self):
        '''
            generate predictions
        '''
        self.predictions = {
            'classes': tf.argmax(
                inputs.self.logits,
                axis=1),
            'probabilities': tf.nn.softmax(
                logits,
                name='softmax_tensor')
        }

    def calculate_loss(self):
        '''
            calculate loss for both train and eval modes
        '''
        self.onehot_labels = tf.one_hot(
            indices=tf.cast(labels, tf.int32),
            depth=10)
        self.loss = tf.losses.softmax_cross_entropy(
            onehot_labels=self.onehot_labels,
            logits=self.logits)

        if mode == tf.estimator.ModeKeys.Train:
            self.optimizer = tf.train.GradientdescentOptimizer(learing_rate=0.001)
            self.train_op = optimizer.minimize(
                loss=self.loss,
                global_step=tf.train.get_global_step())

            return tf.estimator.EstimatorSpec(
                mode=self.mode,
                loss=self.loss,
                train_op=self.train_op)

        self.eval_metric_ops = {
            'accuracy': tf.metrics.accuracy(
                labels=self.labels,
                predictions=self.predictions['classes'])
        }

        return tf.esimator.EsimatorSpec(
            mode=self.mode,
            loss=self.loss,
            eval_metric_ops=self.eval_metric_ops)

cnn = CNN()
