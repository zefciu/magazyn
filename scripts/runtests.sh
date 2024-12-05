#!/usr/bin/bash
set -e
flake8 magazyn test
mypy magazyn test
CONFIG_FILE=config_test.yaml alembic upgrade head
CONFIG_FILE=config_test.yaml pytest --cov=magazyn
