#!/usr/bin/env bash

# 
set -v

rm -rf ./venv
python3 -m venv venv
source venv/bin/activate
which pip
pip install -r requirements.txt
