from flask import request
from app.helpers.jwt_helper import JWTHelper
from app.helpers.response_helper import ResponseHelper


class TokenMiddleware:
  def validate_token(self, response_helper: ResponseHelper):
    access_token = request.headers.get('Authorization')
    if access_token is None: return response_helper.set_to_failed('Access Token should be provided', 401)
    JWTHelper().decode_token(token=access_token, verify_signature=True)