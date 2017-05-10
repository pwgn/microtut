import sys
import requests

from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from flask_security import auth_token_required
from core import db, security, user_datastore
from users import Users
app = Flask(__name__)
bp = Blueprint('auth', __name__, url_prefix='/auth')

users = Users()

@bp.route("/validate", methods=["GET"])
@auth_token_required
def validate():
    return 'ok'

if __name__ == "__main__":
    port = 7000

    # Read port from commandline
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    # Setup app
    app.register_blueprint(bp)
    app.config.from_object('settings')

    db.init_app(app)
    db.create_all(app=app)

    security.init_app(app, user_datastore)

    if app.debug:
        CORS(app, resources=r'/*',
                 allow_headers=['Content-Type', 'Authentication'],
                 supports_credentials=True)

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
