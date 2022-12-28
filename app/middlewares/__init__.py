from app.helpers.response_helper import ResponseHelper
from app.middlewares.token_middleware import TokenMiddleware

class Middleware:
  def __call__(self):
    response_helper = ResponseHelper()
    try:
      # TODO: run validations here
      TokenMiddleware().validate_token(response_helper=response_helper)
    except Exception as e:
      response_helper.set_to_failed(str(e))
    finally:
      return response_helper.get_response()
