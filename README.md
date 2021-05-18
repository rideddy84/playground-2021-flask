```
$ python3 -m venv venv
$ . venv/bin/activate
$ export FLASK_APP=hello.py
$ flask run
```
```
$ celery -A hello.celery worker
```
```
$ pip3 freeze > requirements.txt
$ pip3 install -r requirements.txt
```