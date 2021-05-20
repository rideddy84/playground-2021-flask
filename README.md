```
$ python3 -m venv venv
$ . venv/bin/activate
$ export FLASK_APP=app.py
$ flask run
```
```
$ celery -A app.celery worker
```
```
$ pip3 freeze > requirements.txt
$ pip3 install -r requirements.txt
```