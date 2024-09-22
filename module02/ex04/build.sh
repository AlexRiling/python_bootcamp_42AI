#!/bin/bash
python -m pip install wheel
# Upgrade pip
python -m pip install --upgrade pip

# Build the package (source and wheel distributions)
python setup.py sdist bdist_wheel

python -m pip install ./dist/my_minipack-1.0.0.tar.gz
python -m pip install ./dist/my_minipack-1.0.0-py3-none-any.whl

