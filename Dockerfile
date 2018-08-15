FROM python:3.6-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements_test.txt

RUN python setup.py install

