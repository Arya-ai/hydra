***********************************************
Thresher
***********************************************
A Cookiecutter Template for a Basic REST API with Basic Bearer Auth + Celery for async long running tasks modified from `tiangolo/full-stack-fastapi-postgresql <https://github.com/tiangolo/full-stack-fastapi-postgresql>`_
This is still a WIP and I plan to add more features as and when they are ready. 

Frameworks Used
###############

* `FastAPI <https://fastapi.tiangolo.com/>`_ + `Uvicorn <https://www.uvicorn.org/>`_
* (Required) `Docker <https://www.docker.com/>`_
* (Required) `Docker-Compose <https://docs.docker.com/compose/>`_
* `Celery <https://docs.celeryproject.org/en/stable/index.html>`_


Installation
############
Make sure you use Python3 environment for cookiecutter

1. To install cookiecutter, run the following command ``pip install cookiecutter``
2. In the directory where you would like to create you project, run ``cookiecutter <github-url-of-cookiecutter-template>``

Input Variables
###############

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* ``author_name``
* ``author_slug``
* ``project_name``
* ``project_slug``
* ``project_superuser_full_name``
* ``project_superuser_email``
* ``project_superuser_password``
* ``postgresql_username``
* ``postgresql_password``
* ``postgresql_database``
* ``rabbitmq_username``
* ``rabbitmq_password``
* ``rabbitmq_vhost``

Run Command
###########

You can use the ./<project-slug>/run file to run some of the useful commands for the project

    ``./run <SERVICE> <COMMAND>``

``./run build``
-----------------
This command is used to build the initial images (local and worker).

``./run rmi``
This command is used to delete the initial images (local and worker).

``./run todos``
---------------
DEV ONLY: To see the active list of todos for the project.


Services
########

``barebones`` Service
---------------------

* ``build``: Builds the ``barebones`` image
* ``rmi``: Removes the ``barebones`` image

``dc`` Service
--------------
This is a list of commands for running the service locally:

* ``up <-d>``: Run containers using docker-compose.
* ``down <-d>``: Shutdown containers using docker-compose
* ``restart <container_name|all>``: Restarts the containers using docker-compose
* ``rmi``: Removes Local images.

``dc-worker`` Service
---------------------
This is list of commands for running the celery worker:

* ``build``: To build only the worker image
* ``rmi``: To delete only the worker image

``app`` Service
---------------
This is a list of commands for interacting with the application

* ``connect``: Bash shell to the application container

Getting Started
---------------
Run the following commands once you have the project setup using the ``cookiecutter`` command:

1. ``./run build``: To build the images that will be used for the project
2. ``./run dc up``: To start the containers
3. Done. There are some sample urls you can try out to see how celery is working with this. You can see the OpenAPI doc on http://localhost/docs
