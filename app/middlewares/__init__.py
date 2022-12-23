from app.helpers.response_helper import ResponseHelper
from app.middlewares.token_middleware import TokenMiddleware

class Middleware:
  def __call__(self):
    response_helper = ResponseHelper()
    try:
      TokenMiddleware().validate_token()
    except Exception as e:
      response_helper.set_to_failed(str(e), 403)
      return response_helper.get_response()