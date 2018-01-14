import tensorflow as tf
import json

'''
    FACE NET
'''
class FaceNet():
    def __init__(self):
        print('created class')

    ########################################
    ''' pre-processing '''
    ########################################

    def get_aligned_data(self):


    ########################################
    '''' start-learning ''''
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
        y_conv, keep_prob = deepnn(x)

    def depp_network(self, x):
        '''
            sets up tg computational graph
            args:
                x is a input tensor with dimensions (n_examples, 10000)
            returns:
                tuple (y, keep_prob)
        '''

        # reshape input tensor
        with tf.name_scope('reshape'):
            x_image = tf.reshape(x, [-1, 100, 100, 1])

        # first convolutional layer
        with tf.name_scope('conv1'):
            W_1 = self.weight_variable([5, 5, 1, 32])
            b_1 = self.bias_variable([32])
            h_conv1 = tf.nn.relu(self.conv2d(x_image, W_1) + b_conv1)

        # first pooling layer
        with.tf.name_scope('pool1'):
            h_pool1 = self.max_pool_2x2(h_conv1)


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
        return tf.nn.max_pool(x, ksise=[1, 2, 2, 1],
            strides=[1, 2, 2, 1], padding='SAME')
            
    def train_network(self):

    def eval_network(self):

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
