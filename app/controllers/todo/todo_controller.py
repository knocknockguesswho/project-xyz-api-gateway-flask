import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper
from app.helpers.jwt_helper import JWTHelper

class TodoController:
  def retrieve_todo_by_session(self):
    """
      Request Query Params
        `limit`: digit string @optional - `?limit=10` (default is 10) -> item per page
        `last_id`: digit string @optional - `?last_id=0` (default is 0)

      return
      - will return data match with `id` as object or dictionary
      - will return empty list if no data match with `id`
    """
    response_helper = ResponseHelper()
    jwt_helper = JWTHelper()
    try:
      decoded_token = jwt_helper.decode_token(token=request.headers.get('Authorization'))
      user_id = decoded_token['user_id']
      limit = request.args.get('limit') # pagination query
      last_id = request.args.get('last_id') # pagination query
      res = requests.get(f'http://127.0.0.1:5002/get-all-by-user-id/{user_id}?limit={limit}&last_id={last_id}')
      res = json.loads(res.text)
      if res['status'] == 404: return response_helper.set_data([])
      if not res['success']: return response_helper.set_to_failed(res['message'], res['status'])
      return response_helper.set_data(res['data'])
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
      return response_helper.get_response()
    finally:
      return response_helper.get_response()
