from functools import wraps
from flask import request, jsonify, session
from app.middlewares.token_validation import TokenValidation
from app.helpers.response_helper import ResponseHelper
from jwt import ExpiredSignatureError

def protected_router_middleware(func):
  @wraps(func)
  def run(*args, **kwargs):
    response_helper = ResponseHelper()
    try:
      TokenValidation().run(request)
      return func(*args, **kwargs)
    except Exception as e:
      msg = str(e)
      status = 401 # error code of 401 only for expired token
      if type(e) != ExpiredSignatureError:
        status = 400
        if len(session.items()) > 0:
          msg += ' - Session Destroyed'
          session.clear() # force browser to remove session cookies if exist
      response_helper.set_to_failed(msg, status)
      res = jsonify(response_helper.__dict__)
      res.status_code = response_helper.status
      return res
  return run


