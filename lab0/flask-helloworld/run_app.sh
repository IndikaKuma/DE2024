#!/bin/bash

# Step 1: install nbconvert library that can be used to covert jupyter notebooks to Python files

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install python3-dev python3-pip python3-venv -y
 # Only create a virtual envrioment if it does not exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv 
fi

. .venv/bin/activate  # for why . instead of source see https://stackoverflow.com/questions/13702425/source-command-not-found-in-sh-shell

pip install -r requirements.txt

python3 app.py
