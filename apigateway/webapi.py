import requests

from core import get_service_url
from flask import Blueprint, request, jsonify, current_app as app
bp = Blueprint('webapi', __name__, url_prefix='/web/api')

@bp.route('/articles/<article_id>', methods=['GET'])
def get_article(article_id):
    discovery_url = app.config['DISCOVERY_SERVICE_URL']

    article_service_url = get_service_url(discovery_url, 'articles', article_id)
    comments_service_url = get_service_url(discovery_url, 'comments', article_id)

    print('get full article', article_service_url, comments_service_url)
    return jsonify('hi')
