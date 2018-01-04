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
        for person in data:
            training_data[person] = []
            testing_data[person] = []
            sets = data[person]
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

    # write json files for dat
    print(testing_data)

seperate_data()
