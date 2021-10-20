FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN pip3 install mysql-connector mysqlclient

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN pip3 install -r requirements.txt

COPY . /code/
