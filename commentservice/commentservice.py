import sys

from flask import Flask, Blueprint
app = Flask(__name__)
bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route("/", methods=["GET"])
def list():
    return "Here are all my comments"

if __name__ == "__main__":
    port = 6001
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    app.register_blueprint(bp)
    app.run(port=port)
