virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=server.py

flask run