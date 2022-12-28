import jwt
from datetime import datetime, timedelta, timezone
from typing import Any
from app.config import config

_ENUM_KEY_ = {
  0: config['SECRET_KEY'].encode('utf-8'),
  1: config['REFRESH_TOKEN_SECRET_KEY'].encode('utf-8')
}

class JWTHelper:
  def __init__(self):
    self.algorithm = 'HS256'

  def _generate_time_now(self):
    return datetime.now(timezone.utc)

  def sign(self, payload: dict[str, Any], exp_mins: float = 2, is_refresh_token: bool = False):
    payload = {
      **payload,
      'iat': self._generate_time_now(),
      'exp': self._generate_time_now() + timedelta(minutes=exp_mins)
    }
    encoded = jwt.encode(payload=payload, key=_ENUM_KEY_[bool(is_refresh_token)], algorithm=self.algorithm)
    return encoded

  def decode_token(self, token: str, is_refresh_token: bool = False, verify_signature: bool = False):
    token = token.replace('Bearer ', '')
    decoded = jwt.decode(jwt=token, key=_ENUM_KEY_[bool(is_refresh_token)], algorithms=self.algorithm, options={'verify_signature': verify_signature})
    return decoded