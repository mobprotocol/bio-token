import tensorflow as tf
import json
import os
import numpy as np
import cv2

'''
    FACE NET
    convolutional neural network
    trains on 100 by 100 pixel labeled pictures
'''

class FaceNet():
    def __init__(self):
        print('created class')
        self.data_path = './processed_data/'

    ########################################
    ''' pre-processing '''
    ########################################

    def process_images(self):
        '''
            load image data into numpy array, convert into tensors
        '''
        # initialize numpy arrays
        self.labels = []
        self.features = []

        # iterate through processed images
        for name in os.listdir(self.data_path):
            if not name.startswith('.'):

                # add to labels array
                print(name)
                self.labels.append(name)

                for image_id in os.listdir('{0}/{1}'.format(self.data_path, name)):
                    # load image from disk
                    image = cv2.imread('{0}/{1}/{2}'.format(self.data_path, name, image_id))

                    # flatten image into pixel array
                    pixel_array = image.flatten()

                    # add to feature array
                    self.features.append(pixel_array)

        self.num_people = len(self.features)


    ########################################
    ''' setup-network '''
    ########################################
    def init_model(self):
        '''
            instantiates model !!! must be called first !!!
        '''

        # input images 100 by 100 pixels
        self.x = tf.placeholder(tf.float32, [None, 10000])

        # target output classes (class for every peson)
        self.y_ = tf.placeholder(tf.float, [None, self.num_people])

        # setup deep cnn
        y_conv, keep_prob = self.deepnn()

    def deep_network(self):
        '''
            sets up tg computational graph
            args:
                x is a input tensor with dimensions (n_examples, 10000)
            returns:
                tuple (y, keep_prob)
        '''

        # reshape input tensor
        with tf.name_scope('reshape'):
            x_image = tf.reshape(self.x, [-1, 100, 100, 1])

        # first convolutional layer
        with tf.name_scope('conv1'):
            W_conv1 = self.weight_variable([5, 5, 1, 100])
            b_conv1 = self.bias_variable([32])
            h_conv1 = tf.nn.relu(self.conv2d(x_image, W_conv1) + b_conv1)

        # first pooling layer
        with tf.name_scope('pool1'):
            h_pool1 = self.max_pool_2x2(h_conv1)

        # second convolutional layer
        with tf.name_scope('conv2'):
            W_conv2 = self.weight_variable([5, 5, 100, 1000])
            b_conv2 = self.bias_variable([1000])
            h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

        # second pooling layer
        with tf.name_scope('pool2'):
            h_pool2 = max_pool_2x2(h_conv2)

        # densely (fully) connected layer
        with tf.name_scope('dense1'):
            W_dense1 = weight_variable([7 * 7 * 1000, 1024])
            b_dense1 = bias_variable([1024])
            h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
            h_dense1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_dense1) + b_dense1)

        with tf.name_scope('dropout'):
            self.keep_prob = tf.placeholder(tf.float32)
            h_dense1_drop = tf.nn.dropout(h_dense1, keep_prob)

        with tf.name_scope('readout'):
            W_read = weight_variable([1024, 10])
            b_read = bias_variable([self.num_people])
            self.y_conv = tf.matmul(h_dense1_drop, W_read) + b_read

    ########################################
    ''' setup-network '''
    ########################################

    def train_network_model(self):
        with tf.name_scope('loss'):
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=self.y_, logits=self.y_conv)

        self.cross_entropy = tf.reduce_mean(cross_entropy)

        with tf.name_scope('adam_optimizer'):
            self.train_step = tf.train.AdamOptimizer(1e-4).minimize(self.cross_entropy)

        with tf.name_scope('accuracy'):
            self.correct_prediction = tf.equal(tf.argmax(self.y_conv, 1), tf.argmax(self.y_, 1))

    def train_network(self):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for in in range(200000):

    ########################################
    ''' start-evaluation '''
    ########################################
    def evaluate_network(self):

        with tf.name_scope('loss'):
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=self.y, logits=self.y_conv)

        cross_enropy = tf.reduce_mean(cross_entropy)

        with tf.name_scope('adam_optimizer'):
            train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

        with tf.name_scope('accuracy'):
            correct_prediction = tf.equal(tf.argmax(self.y_conv, 1), tf.argmax(y_, 1))
            correct_prediction = tc.cast (correct_prediction, tf.float32)

        accuracy = tf.reduce_mean(cross_entropy)

        graph_location = tmpfile.mkdtemp()

        print('Saving graph to: {0}',format(graph_location))

        with tf.Session() as sess:
            for i in range(1000):
                batch = self.batch_data.next_batch(100)
                if i % 100 == 0:
                    train_accuracy = self.accuracy.eval({
                        feed_dict={
                            x: batch[0],
                            y_: batch[1],
                            keep_prob: 1.0 }})
                    print('step {0}, training accuracy '.format(i, train_accuracy))
                self.train_step.run(feed_dic={ x: batch[0], y: batch[1], keep_prob: 0.5 })
            print('test accuracy %g' % accuracy.eval(feed_dict={
                x: self.features, y_: self.labels, keep_prob: 1.0 }))

    ########################################
    ''' util-fns '''
    ########################################

    def weight_variable(self, shape):
        # pick random weights in a truncated normal distribution
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def bias_variable(self, shape):
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    def conv2d(self, x, W):
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
            strides=[1, 2, 2, 1], padding='SAME')

    ########################################

'''

GENERAL ARCHITECTURE:

########################################
CONVOLUTIONAL LAYER
########################################

########################################
POOLING LAYER
########################################

########################################
CONVOLUTIONAL LAYER
########################################

########################################
POOLING LAYER
########################################


'''

face_net = FaceNet()

face_net.process_images()
