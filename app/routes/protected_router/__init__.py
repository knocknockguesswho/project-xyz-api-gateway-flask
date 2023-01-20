from flask import Blueprint
from app.controllers.auth.auth_controller import AuthController
from app.controllers.todo.todo_controller import TodoController
from app.middlewares.protected_router_middleware import protected_router_middleware
# logout *auth* (will destroy session later)
# retrieve user data *user* DONE (REMOVED)
# reset password *user*
# forgot password *user*
# deactivate account *user*
# retrieve todo *todo*
# add todo (validate parent/child id if providded) *todo*
# remove todo *todo*
# done todo *todo*

blueprint = Blueprint('protected_router', __name__)

@blueprint.route('/auth/logout', methods=['POST'])
@protected_router_middleware
def logout(): return AuthController().logout()

@blueprint.route('/todo/self') # prefer get user id from decoded token instead, not using params
@protected_router_middleware
def retrieve_todo_by_session(): return TodoController().retrieve_todo_by_session()
