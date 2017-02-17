import sys

from flask import Flask, Blueprint
app = Flask(__name__)
bp = Blueprint('discoveryservice', __name__, url_prefix='/discoveryservice')


@bp.route('/<service_id>', methods=['get'])
def get_service(service_id):
    print 'Get service: ' + service_id
    return 'Get service: ' + service_id

@bp.route('/<service_id>', methods=['PUT'])
def register_service(service_id):
    print 'Register service: ' + service_id
    return 'Register service: ' + service_id


if __name__ == '__main__':
    port = 6100
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')
    app.run(port=port)
