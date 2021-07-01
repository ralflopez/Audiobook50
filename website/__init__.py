from flask import Flask
from flask.helpers import url_for
from flask_session import Session

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfsfsdfas'

    # configure session
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # register routes
    from .views import views
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix="/api")

    return app