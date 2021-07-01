from flask import Blueprint, render_template
from flask_session import Session
from werkzeug.utils import redirect
from .helpers import login_required

views = Blueprint('views', __name__)

@views.route('/')
def index():
    # from .packages.youtube_data_api import getVideoTranscript

    return render_template('index.html')

@views.route('/book')
def book_invalid():
    return redirect('/')

@views.route('/book/<v_id>')
@login_required
def book(v_id):
    book_details = {
        'title': 'The Art of War',
        'author': 'Sun Tzu'
    }

    return render_template('book.html', book_details=book_details, v_id=v_id)


@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/register')
def register():
    return render_template('register.html')