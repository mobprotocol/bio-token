for now this is a playground for me to learn machine learning ... mostly biometric identity stuff.

biometric classifications seem to peek in accuracy at about 99%

the solution, combine face, ekg, and eeg data --> .01 ^ n

Keep false positives as low as possible, some leniency to false negatives


## Facial Recognition ##

### Data Set: ####
youtube faces data set

https://www.cs.tau.ac.il/~wolf/ytfaces/index.html#download

will need to sign up here to receive access to ftp server

place in `data/youtube_faces/`

####Data Processing: ####
for now i am using json to organize data `person -> videos -> images`

to process raw youtube_faces data into json:

`python3 scripts/data_to_json.py`

--> output writes json to `./processed_data.json`

to organize data into training and testing sets:

`python 3 scripts/seperate_data.py`

--> `training_data.json`

--> `testing_data.json`


Training:

Feature Detection: dlib

Convolutional

## ECG data ##

electrocardiogram using openbci system



250 Hz sample rate
