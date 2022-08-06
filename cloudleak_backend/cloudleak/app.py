from celery import Celery
from flask import Flask
from flask_cors import CORS

from routes.scans.buckets_scanner_api import scans_api


def create_celery_app(app=None):
    flask_app = app or create_flask_app()

    celery_app = Celery(flask_app.import_name)
    celery_app.conf.update(flask_app.config.get("CELERY_CONFIG", {}))

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


def create_flask_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object("config.settings")

    add_extensions(app=flask_app)

    # register APIs.
    flask_app.register_blueprint(scans_api)

    return flask_app


def add_extensions(app):
    """Configuring extensions for flask"""
    CORS(app)

    return None


app = create_celery_app()
