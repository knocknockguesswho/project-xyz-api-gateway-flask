from flask import request
from app.helpers.jwt_helper import JWTHelper


class TokenMiddleware:
  def validate_token(self):
    access_token = request.headers.get('Authorization')
    if access_token is None: raise Exception('Access Token should be provided')
    JWTHelper().decode_token(access_token=access_token, verify_signature=True)