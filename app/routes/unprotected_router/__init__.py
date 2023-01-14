from flask import Blueprint
from app.controllers.auth.auth_controller import AuthController
from app.middlewares.session_middleware import session_middleware

blueprint = Blueprint('unprotected_router', __name__)

@blueprint.route('/auth/login', methods=['POST'])
def login(): return AuthController().login()

@blueprint.route('/auth/register', methods=['POST'])
def register(): return AuthController().register()

@blueprint.route('/auth/refresh-token', methods=['POST'])
@session_middleware
def refresh_token(): return AuthController().refresh_token()
