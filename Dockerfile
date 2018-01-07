FROM python:3

WORKDIR /

RUN pip install -r requirements.txt

ADD /

EXPOSE 3344

CMD ['python': 'scripts/data_to_json.py']

CMD ['python': 'scripts/seperate_data.py']
