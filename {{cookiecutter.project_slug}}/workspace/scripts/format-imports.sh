#!/usr/bin/env sh
set -x

isort --recursive --force-single-line-imports app
sh ./scripts/format.sh