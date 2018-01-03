import os
import json

def create_json_schema():
    """ returns json schema for aligned images data"""
    data_schema = {}
    data_path = './data/youtube_faces/aligned_images_DB/'
    for person in os.listdir(data_path):
        if not person.startswith('.'):
            data_schema[person] = {}
            for imageset in os.listdir(data_path + person):
                if not imageset.startswith('.'):
                    data_schema[person][imageset] = []
                    for image in os.listdir(data_path + person + '/' + imageset):
                        data_schema[person][imageset].append(image)
    return data_schema
def write_schema(schema):
    """ writes schema to json file """
    print('made it here')
    with open('./processed_data.json', 'w') as outfile:
        json.dump(schema, outfile)

schema = create_json_schema()
write_schema(schema)
