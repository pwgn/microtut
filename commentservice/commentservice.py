import sys
import requests

from flask import Flask, Blueprint, jsonify
app = Flask(__name__)
bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route("/", methods=["GET"])
def list():
    return jsonify("Here are all my comments")

if __name__ == "__main__":
    port = 6001
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')

    discoveryServiceRequest = 'http://' + app.config['DISCOVERY_SERVICE_URL'] + '/' + bp.name
    discoveryServiceData = {
        'service_id': bp.name,
        'host': 'localhost',
        'port': port
    }
    response = requests.put(discoveryServiceRequest, json = discoveryServiceData)

    app.run(port=port)
