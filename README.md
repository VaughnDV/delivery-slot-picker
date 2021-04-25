Delivery Slot Picker
====================

slot pickerthat generates a group of dates and delivery slots for selection

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>


## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

`docker-compose up --build`

If all works well, you should be able to create an admin account with:

`docker-compose run backend python manage.py createsuperuser`

For manual testing one should generate delivery slots for the next 4 weeks:

`docker-compose run backend python manage.py generate_delivery_slots`

In production this can be set to run a daily cronjob to ensure that there are always 4 weeks of delivery slots generated


## Running tests

`docker-compose run backend pytest`
