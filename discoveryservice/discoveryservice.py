import sys

from flask import Flask, Blueprint, jsonify, request
from registry import Registry
app = Flask(__name__)
bp = Blueprint('discoveryservice', __name__, url_prefix='/discoveryservice')

registry = Registry()

@bp.route('/<service_id>', methods=['GET'])
def get_service(service_id):
    service = registry.get_service(service_id)
    print(request.get_json())
    return jsonify(service)

@bp.route('/<service_id>', methods=['PUT'])
def register_service(service_id):
    print('register services')
    registry.register_service(service_id, request.get_json())
    return 'Register service: ' + service_id


if __name__ == '__main__':
    port = 6100
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')
    app.run(port=port)
