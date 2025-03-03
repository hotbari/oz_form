from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from app.services.users import (
    create_user, get_all_users, get_user_by_id, update_user, delete_user
)

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix="/signup")


@user_blp.route('/')
class UserCreate(MethodView):
    def post(self):
        user_data = request.json
        return create_user(user_data)

    def get(self):
        return get_all_users()


@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    def get(self, user_id):
        return get_user_by_id(user_id)


@user_blp.route('/admin/<int:user_id>')
class UserModify(MethodView):
    def put(self, user_id):
        user_data = request.json
        return update_user(user_id, user_data)

    def delete(self, user_id):
        return delete_user(user_id)
