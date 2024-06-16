from flask import Blueprint

bp = Blueprint('health', __name__)


@bp.route('/health')
def health_check():
    return '', 204
