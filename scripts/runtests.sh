#!/usr/bin/bash
set -e
flake8 magazyn test
mypy magazyn test
pytest
