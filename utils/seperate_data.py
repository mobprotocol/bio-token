import json
import os
import sys
from logging import ShortLog

'''
    util function to seprate processed_data.json
    training.json
    testing.json

    person --> [...jpgs]
'''

def seperate_data():
    training_data = {}
    testing_data = {}
    file_path = './data/youtube_faces/aligned_images_DB/'
    # open & read processed data json
    with open('./processed_data.json') as json_data:
        data = json.loads(json_data.read())
        # iterate through each person
        for person in data:
            training_data[person] = []
            testing_data[person] = []
            sets = data[person]
            # one set goes to testing the rest are used for training
            for idx, st in enumerate(sets):
                images = os.listdir(file_path + person + '/' + st)
                if idx == len(sets) - 1:
                    for image in images:
                        if not image.startswith('.'):
                            testing_data[person].append(image)

                else:
                    for image in images:
                        if not image.startswith('.'):
                            training_data[person].append(image)

    return (training_data, testing_data)

def write_seperated_data(payloads):
    with open('./training_data.json', 'w') as trainfile:
        json.dump(payloads[0], trainfile)
    with open('./testing_data.json', 'w') as testfile:
        json.dump(payloads[1], testfile)

data_sets = seperate_data()
write_seperated_data(data_sets)
