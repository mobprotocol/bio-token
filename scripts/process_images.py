import os
import cv2
import codecs
# file paths for youtube faces data set
file_path = './data/youtube_faces/aligned_images_DB/'
file_write_path = './data/youtube_faces/face_images_DB/'

# importing pre-trained haar cascade models
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def find_face(image, name):
    '''
        processes image --> face close-up and saves to disk
        args:
            image: cv2 image
            name: string name (also the label)
    '''

    # converting image to white/black scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # using built-in haar cascades from opencv to find faces
    faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)

    # iterate through faces
    for (x, y, w, h) in faces:
        # create rectangle frame around face
        cv2.rectangle(gray_image, (x, y), (x + y, y + h), (255, 0, 0), 2)

        # black/white close-up
        roi_gray = gray_image[y:y+h, x:x+w]
        # color close-up
        roi_color = image[y:y+h, x:x+w]
        # crop image
        face_image = image[y: y+h, x: x+w]

    # display close-up (for sanity check)
    cv2.imshow('image', face_image)
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    # writing image to disk
    cv2.imwrite(file_path + '/face_closeup'  + randint(0, 1e9) +'.jpg', face_image)


def main():
    # iterate through all youtube faces aligned images
    for person in os.listdir(file_path):
        if not person.startswith('.'):
            for image_set in os.listdir(file_path + '/' + person):
                if not image_set.startswith('.'):
                    for image in os.listdir(file_path + '/' + person + '/' + image_set):
                        if not image.startswith('.'):
                            image_view = cv2.imread(file_path + '/' + person + '/' + image_set + '/' + image)
                            face = find_face(image_view, name)

if __name__ == '__main__':
    main()
