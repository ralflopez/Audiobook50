from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)

@api.route('/transcript')
def transcript():
    id = request.args.get('v')

    from .packages.youtube_data_api import getVideoTranscript
    transcript = getVideoTranscript(id)

    return jsonify(transcript)