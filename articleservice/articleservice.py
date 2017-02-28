import sys
import requests

from flask import Flask, Blueprint, jsonify
from articles import Articles
app = Flask(__name__)
bp = Blueprint('articles', __name__, url_prefix='/articles')

articles = Articles()

@bp.route("/", methods=["GET"])
def list():
    arts = articles.list()
    print('articles:', arts)
    return jsonify(arts)

if __name__ == "__main__":
    port = 6000

    # Read port from commandline
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    # Setup app
    app.register_blueprint(bp)
    app.config.from_object('settings')

    # Register to discovery service
    discoveryServiceRequest = 'http://' + app.config['DISCOVERY_SERVICE_URL'] + '/' + bp.name
    discoveryServiceData = {
        'service_id': bp.name,
        'host': 'localhost',
        'port': port
    }
    response = requests.put(discoveryServiceRequest, json = discoveryServiceData)

    # Start app
    app.run(port=port)
