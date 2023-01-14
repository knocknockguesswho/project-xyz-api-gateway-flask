from app.helpers.response_helper import ResponseHelper

class SessionValidation():
  def run(self, sess, response_helper: ResponseHelper):
    if len(sess.items()) == 0:
      response_helper.set_to_failed('Session Invalid', 403)
      raise Exception()