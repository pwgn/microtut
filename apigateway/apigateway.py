import sys
import requests

from flask import Flask, Blueprint, request, jsonify
app = Flask(__name__)
bp = Blueprint('apigateway', __name__, url_prefix='/api')

@bp.route("/<service_id>", defaults={'path': ''})
@bp.route("/<service_id>/<path:path>")
def route(service_id, path):

    # Get the service from the service registry
    discoveryservice_url = 'http://' + '/'.join([app.config['DISCOVERY_SERVICE_URL'], service_id])
    discoveryservice_response = requests.get(discoveryservice_url)

    # Build the service url
    service = discoveryservice_response.json()
    service_url = service['host'] + ':' + str(service['port'])
    service_request_url = 'http://' + '/'.join([service_url, service_id, path])

    # Log some stuff
    print('route:', service_id, path)
    print('json:', request.get_json())
    print('method:', request.method)
    print('service_url:', service_request_url)

    # Forward the request to the service
    service_response = None
    if request.method == 'GET':
        service_response = requests.get(service_request_url, json = request.get_json())
    elif request.method == 'PUT':
        service_response = requests.put(service_request_url, json = request.get_json())

    print ('service_response:', service_response.json())

    return jsonify(service_response.json());

if __name__ == "__main__":
    port = 6101
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')
    app.run(port=port)
