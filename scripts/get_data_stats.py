import json
import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
        retrieves metrics from json schema
    '''

    # read data from disk
    with open('./data.json', 'r') as  outfile:
        data = json.load(outfile)

    # instantiate metrics
    total_identites = 0
    total_photos = 0
    image_count = {}
    max_num_photos = 0

    # iterate through schema
    for name in data:
        # add to identity count
        total_identites += 1
        image_count[name] = 0
        for image_name in data[name]:
            # add to total photos count
            total_photos += 1
            # add to image count
            image_count[name] +=1
            # keep track of max photos for a given identity
            if image_count[name] > max_num_photos:
                max_num_photos = image_count[name]

    # find mean num images
    mean_images = total_photos/total_identites

    # find median num images
    # find standard deviation in identity image distrubition

    # print out metrics to console
    print('###')
    print('total_identites: {0}'.format(total_identites))
    print('mean images: {0}'.format(mean_images))
    print('###')

    # plot bar chart of image distribution
    image_dist = ()
    names = ()
    for name in image_count:
        names = names + (name, )
        image_dist = image_dist + (image_count[name], )

    ind = np.arange(len(image_dist))
    plt.bar(ind, image_dist, align='center', alpha=0.5)
    # plt.ylabel('num images')
    # plt.title('image distribution of identities')
    # plt.xticks(ind, names)
    # plt.yticks(np.arrange(image_dist))
    # plt.Show()

    # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    # y_pos = np.arange(len(objects))
    # performance = [10,8,6,4,2,1]

    # plt.barh(y_pos, performance, align='center', alpha=0.5)
    # plt.yticks(y_pos, objects)
    # plt.xlabel('Usage')
    # plt.title('Programming language usage')
    #
    # plt.show()


if __name__ == '__main__':
    # start script
    main()
