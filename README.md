## Video Processing Pipeline ##

1. `python3 scripts/capture_video.py` [first_name] [last_name]

Captures video via opencv and saves `.avi` --> `./data/captured/raw_video/`

2. `python3 scripts/analyze_video.py` [first_name] [last_name]

Iterates through video and shows face and eye detection from haar cascades

3. `python3 scripts/view_feature_detection.py` [first_name] [last_name]

Iterates through video and shoes feature detection from pre-trained dlib model

4. `python3 scripts/process_yt_data.py`

Aligns and crops youtube_faes data set into face close-ups

--> `./processed_data/first_last/`
