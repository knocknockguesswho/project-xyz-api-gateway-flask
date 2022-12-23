from flask import Blueprint
from app.controllers.todo.todo_controller import TodoController
from app.controllers.user.user_controller import UserController
from app.middlewares import Middleware

middleware = Middleware()

# logout *auth* (will destroy session later)
# retrieve user data *user* DONE
# reset password *user*
# forgot password *user*
# deactivate account *user*
# retrieve todo *todo*
# add todo (validate parent/child id if providded) *todo*
# remove todo *todo*
# done todo *todo*

blueprint = Blueprint('protected_router', __name__)
blueprint.before_request(middleware)
# TODO: need to add middleware to validate
# - security-header

@blueprint.route('/auth/logout', methods=['POST'])
def logout(): return 'ok'

@blueprint.route('/user/profile')
def retrieve_profile(): return UserController().retrieve_profile()
