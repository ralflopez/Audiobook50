from flask import Blueprint, request, jsonify, session
from werkzeug.utils import redirect
from . import db
from .helpers import apology, login_required

api = Blueprint('api', __name__)

@api.route('/transcript')
@login_required
def transcript():
    id = request.args.get('v')

    from .packages.youtube_data_api import getVideoTranscript
    transcript = getVideoTranscript(id)

    return jsonify(transcript)

@api.route('/save', methods=['POST'])
@login_required
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

    return redirect('/profile')


@api.route('/unsave', methods=['POST'])
@login_required
def unsave():
    user_id = session.get('user_id')
    data = request.get_json()

    if not data:
        return apology('Unable to unsave file')

    if not user_id:
        return redirect('/login')
    
    # delete from db
    db.execute('DELETE FROM saves WHERE book_id = ? AND user_id = ?;', data['v_id'], user_id)

    return jsonify({'success': 'Unsaved'})


@api.route('/delete', methods=['POST'])
@login_required
def delete():
    user_id = session.get('user_id')
    data = request.get_json()

    if not data:
        return apology('Unable to delete file')

    if not user_id:
        return redirect('/login')
    
    # delete from db
    db.execute('DELETE FROM books WHERE id = ? AND contributor_id = ?;', data['v_id'], user_id)

    return jsonify({'success': 'Deleted'})