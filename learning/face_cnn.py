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


    def train_network(self):

    def eval_network(self):

    ########################################
