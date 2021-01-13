FROM Ubuntu
FROM python:3.7

WORKDIR /usr/src/app

RUN sudo apt-get update
RUN sudo apt-get upgrade

COPY .requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app




