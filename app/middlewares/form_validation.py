import re
import pycountry
from datetime import datetime
from typing import Any

class SignupFormValidation:
  def __init__(self, schema: dict[str, Any]):
    self.schema = schema

  def name_validation(self):
    first_name = self.schema['first_name']
    last_name = self.schema['last_name']
    if len(first_name) < 1 or len(first_name) > 16:
      raise Exception('First name should be min `1` char(s) and max `16` char(s)')
    if len(last_name) < 1 or len(last_name) > 16:
      raise Exception('Last name should be min `1` char(s) and max `16` char(s)')
    
  def email_validation(self):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, self.schema['email']) is None:
      raise Exception('Invalid email format')
  
  def username_validation(self):
    username: str = self.schema['username']
    regex = re.compile(r'^[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)*$')
    if len(username) < 4 or len(username) > 16:
      raise Exception('Username should be min `4` char(s) and max `16` char(s)')
    if username[0] == '_':
      raise Exception('Username should be started with `alphanumeric` character')
    if re.fullmatch(regex, username) is None:
      raise Exception('Username only allow `alphanumeric` and `_` character')
    
  def password_validation(self):
    regex = re.compile(r'.{8,20}')
    if re.fullmatch(regex, self.schema['password']) is None:
      raise Exception('Password should be min `8` char(s) and max `20` char(s)')
  
  def birth_date_validation(self):
    date = datetime.fromisoformat(self.schema['birth_date'])
    if date.timestamp() > datetime.now().timestamp(): raise Exception('Invalid birth date')
    
  def country_code_validation(self):
    country = pycountry.countries.get(alpha_2=self.schema['country_code'])
    if country is None: raise Exception('Invalid country code')

  def run(self):
    self.email_validation()
    self.username_validation()
    self.name_validation()
    self.birth_date_validation()
    self.country_code_validation()
    self.password_validation()