*****************************
{{cookiecutter.project_slug}}
*****************************

Backend Requirements
####################

* `Docker <https://www.docker.com/>`_
* `docker-compose <https://docs.docker.com/compose/>`_

Getting Started
###############
Run the following commands once you have the project setup:

1. ``make``: To build the images that will be used for the project
2. ``make up|daemon``: To start the containers
3. Done. There are some sample urls you can try out to see how celery is working with this. You can see the OpenAPI doc on http://localhost/docs. A .secrets file is created to store all the auto-generated/filled passwords