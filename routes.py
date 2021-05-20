from app import app
from celery_functions import add_together


@app.route('/')
def hello_world():
    add_together.delay(23, 42)
    return 'Hello, World!'
