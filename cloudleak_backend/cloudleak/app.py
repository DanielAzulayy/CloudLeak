from celery import Celery
from flask import Flask
from flask_cors import CORS


def create_celery(flask_app=None):
    flask_app = flask_app or create_app()

    celery = Celery(flask_app.import_name)
    celery.conf.update(flask_app.config.get("CELERY_CONFIG", {}))

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(register_blueprints=True):
    flask_app = Flask(__name__)

    flask_app.config.from_object("config.settings.CeleryConfig")
    flask_app.config.from_object("config.settings.MongoConfig")

    configure_extensions(app=flask_app)

    if register_blueprints:
        from cloudleak.routes.scans.buckets_scanner_api import scans_api

        flask_app.register_blueprint(scans_api)

    return flask_app


def configure_extensions(app):
    """Configuring extensions for flask"""
    CORS(app)

    return None


celery_app = create_celery()
