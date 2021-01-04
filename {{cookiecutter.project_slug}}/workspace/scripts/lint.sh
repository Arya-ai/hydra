#!/usr/bin/env sh

set -x

mypy app
black app --check
isort --recursive --check-only app
flake8