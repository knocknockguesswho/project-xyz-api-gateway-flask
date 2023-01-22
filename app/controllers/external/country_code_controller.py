import json
import requests
from app.helpers.response_helper import ResponseHelper

class CountryCodeController:
  def retrieve_all_country_codes(self):
    response_helper = ResponseHelper()
    try:
      res = requests.get('https://api.first.org/data/v1/countries')
      res = json.loads(res.text)
      if 'data' in res: return response_helper.set_data(res['data'])
    except Exception as e:
      msg = str(e)
      status = 400
      response_helper.set_to_failed(msg, status)
    finally:
      return response_helper.get_response()