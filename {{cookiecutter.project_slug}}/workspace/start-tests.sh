#!/usr/bin/env sh
set -e

python ./app/tests_pre_start.py

bash ./scripts/tests.sh "$@"