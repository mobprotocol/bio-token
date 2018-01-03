import os

def create_json_schema():
    data_schema = {}
    data_path = './data/youtube_faces/aligned_images_DB/'
    for person in os.listdir(data_path):
        if person.startswith('.'):
            continue
        for imageset in os.listdir(data_path + person):
            for image in os.listdir(data_path + person + '/' + imageset):
                print(image)

create_json_schema()
