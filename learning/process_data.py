import os
import cv2
import numpy as np
import tensorflow as tf

data_path = './processed_data'

def main():
    # for name in os.listdir(data_path):
    #     if not name.startswith('.'):
    #         for image_name in os.listdir('{0}/{1}'.format(data_path, name)):
    #             image = cv2.imread('{0}/{1}/{2}'.format(data_path, name, image_name))

    filename_queue = tf.train.string_input_producer(
        tf.train.match_filenames_once('./processed_data/*.jpg'))

    image_reader = tf.WholeFileReader()

    _, image_file = image_reader.read(filename_queue)

    image = tf.image.decode_jpeg(image_file)

    with tf.Session() as sess:
        tf.local_variables_initializer().run()

        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        image_tensor = sess.run([image])

        print(image_tensor)

        coord.request_stop()
        coord.join(threads)


if __name__ == '__main__':
    # run script
    main()
