FROM python:3

RUN pip install -r requirements.txt

ADD .

EXPOSE 3344
