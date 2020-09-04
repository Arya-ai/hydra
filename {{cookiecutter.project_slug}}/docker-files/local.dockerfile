FROM arya/{{cookiecutter.project_slug}}-api:barebones

WORKDIR /app/workspace

CMD ["./start.sh"]