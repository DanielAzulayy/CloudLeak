from flask import Flask
from celery import Celery
from routes.scans.buckets_scanner import scans_api


def create_celery_app(app=None):
    flask_app = app or create_flask_app()

    celery_app = Celery(flask_app.import_name)
    celery_app.conf.update(flask_app.config.get('CELERY_CONFIG', {}))


def create_flask_app():
    flask_app = Flask(__name__)
    

    flask_app.register_blueprint(scans_api)
