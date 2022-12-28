import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper
from app.helpers.jwt_helper import JWTHelper

class UserController:
  def retrieve_profile(self):
    response_helper = ResponseHelper()
    jwt_helper = JWTHelper()
    try:
      # get user id from decoded access token
      access_token = request.headers.get('Authorization')
      user_id = jwt_helper.decode_token(token=access_token)['user_id']
      res = requests.get(f'http://127.0.0.1:5001/get-by-id/{user_id}')
      res = json.loads(res.text)
      response_helper.set_data(res['data'])
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()