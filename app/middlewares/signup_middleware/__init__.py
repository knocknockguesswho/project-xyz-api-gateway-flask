from functools import wraps
from flask import jsonify, request
from app.middlewares.form_validation import SignupFormValidation
from app.helpers.response_helper import ResponseHelper
from app.helpers.schema_helper import SignupFormSchema

def signup_middleware(func):
  @wraps(func)
  def run(*args, **kwargs):
    response_helper = ResponseHelper()
    try:
      schema = SignupFormSchema()
      obj = vars(schema)
      # validate if data is included in our form schema
      for x in obj.keys():
        if x in request.form: obj[x] = request.form[x]
        else: raise Exception(f'Field `{x}` is required')
      SignupFormValidation(schema=obj).run()
      return func(*args, **kwargs)
    except Exception as e:
      msg = str(e)
      status = 400
      if e.__cause__ is not None:
        msg = str(e.__cause__)
        status = 500
      response_helper.set_to_failed(msg, status)
      res = jsonify(response_helper.__dict__)
      res.status_code = response_helper.status
      return res
  return run


