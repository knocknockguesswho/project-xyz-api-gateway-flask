from flask import Blueprint
from app.controllers.auth.auth_controller import AuthController

blueprint = Blueprint('unprotected_router', __name__)

@blueprint.route('/auth/login', methods=['POST'])
def login(): return AuthController().login()

@blueprint.route('/auth/register', methods=['POST'])
def register(): return AuthController().register()

@blueprint.route('/auth/refresh-token', methods=['POST'])
def refresh_token(): return AuthController().refresh_token()
