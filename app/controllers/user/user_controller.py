import json
import requests
from flask import request
from app.helpers.response_helper import ResponseHelper
from app.helpers.jwt_helper import JWTHelper

class UserController:
  def find_friend(self, **params):
    return