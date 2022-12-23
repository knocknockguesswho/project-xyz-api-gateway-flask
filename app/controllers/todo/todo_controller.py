import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper

class TodoController:
  def retrieve_todo(self, **params):
    response_helper = ResponseHelper()
    return response_helper.get_response()
