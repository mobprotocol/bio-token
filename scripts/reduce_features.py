import json
import os
import cv2
import dlib
from feature_detection import detect_features

def main():
    '''
        extracts feature landmarks from processed data
        returns:
            json representation of feature data
            person --> [feature_set1, ... ]
    '''

    # make sure data path exists
    assert os.path.exists('./processed_data')

    # json schema
    feature_data = {}

    # iterate through data
    for person in os.listdir('./processed_data')
        feature_data[person] = []
        for image_name in os.listdir('./processed_data/{0}'.format(person)):

            # load image into cv2 object
            image = cv2.imread('./processed_data/{0}/{1}'.format(person, image_name))

            # find landmark features with util fn
            features = detect_features()

            # append feature set to json object
            feature_data[person].append(features)

    # write json to ./feature_data.json
    with open('./feature_data.json', 'w') as outfile:
        json.dump(feature_data, outfile)

if __name__ == '__main__':
    # start script
    main()
