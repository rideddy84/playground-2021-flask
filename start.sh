. venv/bin/activate
export FLASK_APP=app.py
celery -A app.celery worker &
flask run
