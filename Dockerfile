# pull official base image
FROM ubuntu:latest
MAINTAINER Vladislav

RUN apt-get update -qy
RUN apt-get install -qy python3.10 python3-pip python3.10-dev

# set work directory
WORKDIR /usr/src/app
# copy project
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3","manage.py"]