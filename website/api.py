from flask import Blueprint, request, jsonify, session
from werkzeug.utils import redirect
from . import db
from .helpers import apology

api = Blueprint('api', __name__)

@api.route('/transcript')
def transcript():
    id = request.args.get('v')

    from .packages.youtube_data_api import getVideoTranscript
    transcript = getVideoTranscript(id)

    return jsonify(transcript)

@api.route('/save', methods=['POST'])
def save():
    user_id = session.get('user_id')
    data = request.get_json()

    if not data:
        return apology('Unable to save file')

    if not user_id:
        return redirect('/login')
    
    # check if book exist
    rows = db.execute('SELECT title FROM books WHERE id = ?', data['v_id'])
    if not len(rows):
        return apology('Book not found')

    db.execute('INSERT INTO saves (user_id, book_id) VALUES (? , ?)', user_id, data['v_id'])

    return jsonify({'title': rows[0]['title']})