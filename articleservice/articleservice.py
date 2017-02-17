import sys

from flask import Flask, Blueprint
app = Flask(__name__)
bp = Blueprint('articles', __name__, url_prefix='/articles')


@bp.route("/", methods=["GET"])
def list():
    return "Here are all my articles"

if __name__ == "__main__":
    port = 6000
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.config.from_object('settings')
    app.run(port=port)
