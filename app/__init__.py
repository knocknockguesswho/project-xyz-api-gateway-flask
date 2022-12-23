from flask import Flask
from app.routes import unprotected_router, protected_router

app = Flask(__name__)

url_prefix = '/v1'
app.register_blueprint(unprotected_router.blueprint, url_prefix=url_prefix)
app.register_blueprint(protected_router.blueprint, url_prefix=url_prefix)