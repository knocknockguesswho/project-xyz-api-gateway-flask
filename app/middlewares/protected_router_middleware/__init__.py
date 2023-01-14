from functools import wraps
from flask import request, jsonify
from app.middlewares.token_validation import TokenValidation
from app.helpers.response_helper import ResponseHelper
from jwt import ExpiredSignatureError

def protected_router_middleware(func):
  @wraps(func)
  def run(*args, **kwargs):
    response_helper = ResponseHelper()
    try:
      TokenValidation().run(request, response_helper)
      return func(*args, **kwargs)
    except Exception as e:
      if e.__cause__ is not None: response_helper.set_to_failed(str(e), 500)
      if type(e) == ExpiredSignatureError: response_helper.set_to_failed(str(e), 401)
      res = jsonify(response_helper.__dict__)
      res.status_code = response_helper.status
      return res
  return run


