from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from init import make_celery

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
db = SQLAlchemy(app)
celery = make_celery(app)

import models
import routes
