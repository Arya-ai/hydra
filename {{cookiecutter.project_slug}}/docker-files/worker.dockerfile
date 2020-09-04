FROM arya/{{cookiecutter.project_slug}}-worker:barebones

WORKDIR /app/workspace

CMD ["./start-worker.sh"]
