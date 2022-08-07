from celery import Celery
from flask import Flask
from flask_cors import CORS


def make_celery(flask_app=None):
    flask_app = flask_app or create_app()

    celery_app = Celery(flask_app.import_name)
    celery_app.conf.update(flask_app.config.get("CELERY_CONFIG", {}))

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


def create_app(register_blueprints=True):
    flask_app = Flask(__name__)
    flask_app.config.from_object("config.settings")

    configure_extensions(app=flask_app)

    if register_blueprints:
        from cloudleak.routes.scans.buckets_scanner_api import scans_api
        flask_app.register_blueprint(scans_api)

    return flask_app


def configure_extensions(app):
    """Configuring extensions for flask"""
    CORS(app)

    return None


app = create_app()
