import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper
from app.helpers.jwt_helper import JWTHelper

class AuthController:
  def register(self):
    """
    Request Form
      `first_name`: str max 50char @required
      `last_name`: str max 50char @required
      `password`: str max 32char @required
      `username`: str max 32char @required @unique
      `email`: str max 50char @required @unique
      `avatar`: str max 512char @required
      `birth_date`: date string @required `YYYY-mm-dd`
      `country_code`: str max 2char @required
    """
    response_helper = ResponseHelper()
    try:
      res = requests.post(
          'http://127.0.0.1:5001/add',
          data={
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'password': request.form['password'],
            'username': request.form['username'],
            'email': request.form['email'],
            'avatar': request.form['avatar'],
            'birth_date': request.form['birth_date'],
            'country_code': request.form['country_code'],
          }
        )
      res = json.loads(res.text)
      if not res['success']: return response_helper.set_to_failed(res['message'], res['status'])
      return response_helper.remove_data()
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()

  def login(self):
    """
    Request Form
      `username`: str max 32char @required @unique
      `password`: str max 32char @required
    """
    response_helper = ResponseHelper()
    jwt_helper = JWTHelper()
    try:
      res = requests.post('http://127.0.0.1:5001/check-credential', data={'username': request.form['username'], 'password': request.form['password']})
      res = json.loads(res.text)
      if not res['success']: return response_helper.set_to_failed(res['message'], res['status'])
      payload = {'user_id': res['data']['id']}
      refresh_token = jwt_helper.sign(payload=payload, exp_mins=1, is_refresh_token=True)
      return response_helper.set_data({'refresh_token': refresh_token})
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()

  def refresh_token(self):
    """
    Request Form
      `refresh_token`: str
    """
    response_helper = ResponseHelper()
    jwt_helper = JWTHelper()
    access_token_expires = 60 * 24 * 7 #a week
    refresh_token_expires = 60 * 24 * 30 #a month
    try:
      # TODO: 
      # client need to encrypt refresh token
      # client need to store encrypted refresh token on session storage
      # server will receive encrypted refresh token from client
      # need to decrypt encrypted refresh token later
      decoded = jwt_helper.decode_token(request.form['refresh_token'])
      payload = {'user_id': decoded['user_id']}
      access_token = jwt_helper.sign(payload=payload, exp_mins=access_token_expires)
      refresh_token = jwt_helper.sign(payload=payload, exp_mins=refresh_token_expires, is_refresh_token=True)
      return response_helper.set_data({'access_token': access_token, 'refresh_token': refresh_token})
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()