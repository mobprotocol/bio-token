import json
import matplotlib.pyplot as plt

def main():
    '''
        retrieves metrics from json schema
    '''

    # read data from disk
    with open('./data.json', 'r') as  outfile:
        data = json.load(outfile)

    # instantiate metrics
    total_identites = 0
    image_count = {}

    # iterate through schema
    for name in data:
        total_identites += 1
        image_count[name] = 0
        for image_name in data[name]:
            image_count[name] +=1

    # print out metrics to console
    print('###')
    print('total_identites: {0}'.format(total_identites))
    print('###')

if __name__ == '__main__':
    # start script
    main()
