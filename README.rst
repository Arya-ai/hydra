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

About
########

The template uses the following components:

* NGINX: The Nginx container serves as a load balancer for the backend container.
* Backend API: This is a FastAPI + Gunicorn container which runs multiple workers to serve as the API endpoint. This is exposed to the Nginx container.
* Backend Worker: This container contains the celery workers which process the celery tasks published by the API asynchronously. 
* PostgreSQL: Serves as the DB for the API as well as Celery, which uses it to keep track of results from the Celery tasks
* RabbitMQ: Serves as the message broker to distribute celery tasks among the Celery workers.

More details
############

More details are mentioned in the README.rst file inside the project directory.
