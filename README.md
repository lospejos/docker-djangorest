# docker-djangorest
Sandbox to learn django-rest-framework and docker

## Dependencies
docker and docker-compose

## Local deployment

    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    docker-compose up


What it does:

-   Install docker and proceed with initial db migrations
-   Create a super user for api ui and admin access
-   Run the postgres image and the web application

It should now be accessible on http://0.0.0.0:8000
