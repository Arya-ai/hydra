*****************************
{{cookiecutter.project_slug}}
*****************************

Backend Requirements
####################

* `Docker <https://www.docker.com/>`_
* `docker-compose <https://docs.docker.com/compose/>`_

Backend Local Development
#########################
Follow the given steps to regenerate the project:

1. Provide server.crt and server.key files in the resources/nginx/certs directory
2. Use the ``run`` script to interact with the application

``run`` Script
##############
The following are the commands you can work with:


#. **Barebones Image**: The barebones image is the first image constructed to install the necessary packages for the application to run. **This image is needed for both the production as well as local images to work**

   #. ``./run barebones build``: Builds the barebones image.
   #. ``./run barebones rmi``: Deletes the barebones image.

#. **Local Image**: The local image is for running in development. It allows the user to modify on the go due to shared volumes.

   #. ``./run dc up|down|restart``: Starts/Stops/Restarts docker containers/images
   #. ``./run dc rmi``: Deletes the local image

#. **Application**: All commands related to the application. ``./run application connect`` starts a shell connection to the container

#. **ToDos**: Finds all ToDo's in the application (for development) - ``./run todo``