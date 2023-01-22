import json
import requests
from flask import request, session
from app.helpers.response_helper import ResponseHelper
from app.helpers.jwt_helper import JWTHelper
from app.config import USER_SERVICE_URL

access_token_expires = 60 * 24 #a day
class AuthController:
  def login(self):
    """
    Request Form
      `username`: str max 32char @required @unique
      `password`: str max 32char @required
    """
    response_helper = ResponseHelper()
    jwt_helper = JWTHelper()
    try:
      res = requests.post(f'{USER_SERVICE_URL}/check-credential', data={'username': request.form['username'], 'password': request.form['password']})
      res = json.loads(res.text)
      if not res['success']: return response_helper.set_to_failed(res['message'], res['status'])
      user_id = res['data']['id']
      payload = {'user_id': user_id}
      access_token = jwt_helper.sign(payload=payload, exp_mins=access_token_expires)
      session.permanent = True
      session['user_id'] = user_id
      session['is_login'] = 1

      user = requests.get(f'{USER_SERVICE_URL}/get-by-id/{user_id}')
      user = json.loads(user.text)
      return response_helper.set_data({'access_token': access_token, **user})
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()

  def refresh_token(self):
    response_helper = ResponseHelper()
    jwt_helper = JWTHelper()
    try:
      payload = {'user_id': session['user_id']}
      access_token = jwt_helper.sign(payload=payload, exp_mins=access_token_expires)
      return response_helper.set_data({'access_token': access_token})
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()

  def logout(self):
    response_helper = ResponseHelper()
    try:
      response_helper.message = 'logout success'
      session.clear()
      response_helper.remove_data()
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()
