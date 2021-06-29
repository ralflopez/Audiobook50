from flask import Blueprint, render_template
from flask_session import Session

views = Blueprint('views', __name__)

@views.route('/')
def index():
    # from .packages.youtube_data_api import getVideoTranscript

    return render_template('index.html')