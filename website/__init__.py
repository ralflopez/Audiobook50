from flask import Flask
from flask_session import Session

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfsfsdfas'

    # configure session
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = 'filesystem'

    # register routes
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app