from flask import Request
from app.helpers.jwt_helper import JWTHelper


class TokenValidation():
  def run(self, request: Request):
    if request.headers.get('Authorization') is None: raise Exception('Access Token should be provided')
    return JWTHelper().decode_token(token=request.headers.get('Authorization'), verify_signature=True)