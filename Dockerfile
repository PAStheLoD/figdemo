FROM python:3.4
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
