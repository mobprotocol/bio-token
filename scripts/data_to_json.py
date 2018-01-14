import os
import json

def main():
    '''
        script creates json scheme out of processed data
        first_last --> [.jpg, ...]
    '''

    # make sure processed_data exists
    assert os.path.exists('./processed_data')
    assert len(os.listdir('./processed_data')) > 0

    # instantiate data obejct
    data = {}

    # iterate through data
    for name in os.listdir('./processed_data'):
        if not name.startswith('.'):
            data[name] = []
            for image_name in os.listdir('./processed_data/{0}'.format(name)):
                if not image_name.startswith('.'):
                    data[name].append(image_name)

    # write json object to disk
    with open('./data.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':
    # start script
    main()
