# pull official base image
FROM python:3.9.0-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

RUN apk add --no-cache tzdata
ENV TZ America/Santiago


# copy project
COPY . /usr/src/app/


