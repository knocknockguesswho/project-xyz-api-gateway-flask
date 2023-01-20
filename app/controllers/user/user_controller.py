import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper
from app.helpers.jwt_helper import JWTHelper

class UserController:
  def find_user_by_username(self, **params):
    response_helper = ResponseHelper()
    username = params['username']
    try:
      res = requests.get(f'http://127.0.0.1:5001/get-by-username/{username}')
      res = json.loads(res.text)
      if not res['success']: return response_helper.set_to_failed(res['message'], res['status'])
      return response_helper.set_data(res['data'])
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()

  def find_friend(self, **params):
    return