sudo apt update

sudo apt install python3.10-venv

python3 -m venv .myvenv

. .myvenv/bin/activate

pip install -r requirements_dev.txt

python -m pytest --junitxml=test_log.xml ./tests