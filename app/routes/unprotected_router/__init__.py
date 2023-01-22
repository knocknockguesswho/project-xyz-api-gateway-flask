from flask import Blueprint
from app.controllers.auth.auth_controller import AuthController
from app.controllers.user.user_controller import UserController
from app.controllers.external.country_code_controller import CountryCodeController
from app.middlewares.session_middleware import session_middleware
from app.middlewares.signup_middleware import signup_middleware

blueprint = Blueprint('unprotected_router', __name__)

@blueprint.route('/auth/login', methods=['POST'])
def login(): return AuthController().login()

@blueprint.route('/user/signup', methods=['POST'])
@signup_middleware
def signup(): return UserController().signup()

@blueprint.route('/auth/refresh-token', methods=['POST'])
@session_middleware
def refresh_token(): return AuthController().refresh_token()

@blueprint.route('/user/find-user-by-username/<string:username>')
def find_user_by_username(username: str): return UserController().find_user_by_username(username=username)

@blueprint.route('/external/country-code')
def retrieve_all_country_codes(): return CountryCodeController().retrieve_all_country_codes()