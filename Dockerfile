FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker-django-test
WORKDIR /docker-django-test
ADD requirements.txt /docker-django-test
RUN pip install -r requirements.txt
ADD . /docker-django-test/
