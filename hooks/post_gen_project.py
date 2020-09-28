import subprocess

SECRETS_FILENAME = ".secrets"
SECRETS_CONTENT = """Project Secret Key: {{cookiecutter.project_secret_key}}

{{cookiecutter.project_name}} First Super-User Email: {{cookiecutter.project_superuser_email}}
{{cookiecutter.project_name}} First Super-User Password: {{cookiecutter.project_superuser_password}}


PostgreSQL Root Password: {{cookiecutter.postgresql_root_password}}
PostgreSQL First User Password: {{cookiecutter.postgresql_password}}

RabbitMQ Password: {{cookiecutter.rabbitmq_password}}
"""

def write_secrets():
    with open(SECRETS_FILENAME, 'w') as f:
        f.write(SECRETS_CONTENT)

def init_git():
    subprocess.call(['git', 'init'], stdout=subprocess.DEVNULL)


def add_all():
    subprocess.call(['git', 'add', '*'], stdout=subprocess.DEVNULL)


def commit():
    subprocess.call(['git', 'commit', '-m', 'Initial Commit'], stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    write_secrets()
    print("# Created .secrets file for reference")
    init_git()
    add_all()
    commit()
