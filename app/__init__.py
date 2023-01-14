from flask import Flask
from flask_cors import CORS
from app.routes import unprotected_router, protected_router
from app.config import config
from datetime import timedelta

app = Flask(__name__)
app.secret_key = config['SECRET_KEY']
app.config.update(
    SESSION_COOKIE_NAME='_xyz_sess',
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_REFRESH_EACH_REQUEST=False,
    PERMANENT_SESSION_LIFETIME=timedelta(days=30)
)
CORS(app=app, origins='*', supports_credentials=True)

url_prefix = '/v1'
app.register_blueprint(unprotected_router.blueprint, url_prefix=url_prefix)
app.register_blueprint(protected_router.blueprint, url_prefix=url_prefix)
