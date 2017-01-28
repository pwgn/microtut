from flask import Flask, Blueprint
app = Flask(__name__)
bp = Blueprint('articles', __name__, url_prefix='/articles')


@bp.route("/", methods=["GET"])
def list():
    return "Here are all my articles"

if __name__ == "__main__":
    app.register_blueprint(bp)
    app.run()
