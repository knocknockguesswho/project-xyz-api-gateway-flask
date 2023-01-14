from flask import Request
from app.helpers.jwt_helper import JWTHelper
from app.helpers.response_helper import ResponseHelper


class TokenValidation():
  def run(self, request: Request, response_helper: ResponseHelper):
    if request.headers.get('Authorization') is None:
      response_helper.set_to_failed('Access Token should be provided', 401)
      raise Exception()
    return JWTHelper().decode_token(token=request.headers.get('Authorization'), verify_signature=True)