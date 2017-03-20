import sys
import requests

from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from comments import Comments
app = Flask(__name__)
bp = Blueprint('comments', __name__, url_prefix='/comments')

comments = Comments()

@bp.route("/<thread_id>", methods=["GET"])
def get_thread(thread_id):
    thread = comments.get_thread(thread_id)
    print('get_thread:', thread_id, thread)
    return jsonify({'thread': thread})

@bp.route("/<thread_id>", methods=["PUT"])
def add(thread_id):
    json_data = request.get_json()
    added_comment = comments.add(thread_id, json_data)
    print('added_comment:', added_comment)
    return jsonify({'comment': added_comment})


if __name__ == "__main__":
    port = 6001
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')

    if app.debug:
        CORS(app, resources=r'/*',
                 allow_headers=['Content-Type', 'Authentication'],
                 supports_credentials=True)

    discoveryServiceRequest = 'http://' + app.config['DISCOVERY_SERVICE_URL'] + '/' + bp.name
    discoveryServiceData = {
        'service_id': bp.name,
        'host': 'localhost',
        'port': port
    }
    response = requests.put(discoveryServiceRequest, json = discoveryServiceData)

    app.run(port=port)
