import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper
from app.config import USER_SERVICE_URL

class UserController:
  def find_user_by_username(self, **params):
    response_helper = ResponseHelper()
    username = params['username']
    try:
      res = requests.get(f'{USER_SERVICE_URL}/get-by-username/{username}')
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
  
  def signup(self):
    """
    Request Form
      `first_name`: str max 50char @required
      `last_name`: str max 50char @required
      `password`: str max 32char @required
      `username`: str max 32char @required @unique
      `email`: str max 50char @required @unique
      `birth_date`: date string @required (isoformat) `YYYY-mm-dd` or `YYYY-mm-dd HH:MM:SS`
      `country_code`: str max 2char @required
    """
    response_helper = ResponseHelper()
    try:
      res = requests.post(
        f'{USER_SERVICE_URL}/add',
        data={
          'first_name': request.form['first_name'],
          'last_name': request.form['last_name'],
          'password': request.form['password'],
          'username': request.form['username'],
          'email': request.form['email'],
          'avatar': '', # taken out from request form due to auth issue. TODO: will be added later on update_profile method/api
          'birth_date': request.form['birth_date'],
          'country_code': request.form['country_code'],
        }
      )
      res = json.loads(res.text)
      if not res['success']:
        msg = res['message']
        if res['status'] == 409:
          field_name = msg[msg.find('for key \'users.'):-1].replace('for key \'users.','')
          msg = f'duplicate-{field_name}'
        return response_helper.set_to_failed(msg, res['status'])
      return response_helper.remove_data()
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()