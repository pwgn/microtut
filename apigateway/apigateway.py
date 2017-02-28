import sys
import requests

from core import get_service_url
from flask import Flask, Blueprint, request, jsonify
app = Flask(__name__)
bp = Blueprint('apigateway', __name__, url_prefix='/api')

allowed_methods = ['GET', 'POST', 'PUT']

@bp.route("/<service_id>", defaults={'path': ''}, methods=allowed_methods)
@bp.route("/<service_id>/<path:path>", methods=allowed_methods)
def route(service_id, path):
    discovery_url = app.config['DISCOVERY_SERVICE_URL']

    # Get service url from discovery service
    service_url = get_service_url(discovery_url, service_id, path)

    # Log some stuff
    print('route:', service_id, path)
    print('json:', request.get_json())
    print('method:', request.method)
    print('service_url:', service_url)

    # Forward the request to the service
    service_response = None
    if request.method == 'GET':
        service_response = requests.get(service_url, json = request.get_json())
    elif request.method == 'POST':
        service_response = requests.post(service_url, json = request.get_json())
    elif request.method == 'PUT':
        service_response = requests.put(service_url, json = request.get_json())

    print ('service_response:', service_response.json())

    return jsonify(service_response.json());

if __name__ == "__main__":
    port = 6101
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')
    app.run(port=port)
