from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required

from models import Role, User
from serializers import RoleSchema, UserSchema

role_routes = Blueprint('role_routes', __name__)


@role_routes.route('/roles', methods=['GET'])
@jwt_required()
def index():
    roles = Role.query.all()
    role_schema = RoleSchema(many=True)  # Use many=True for lists
    serialized_roles = role_schema.dump(roles)
    return jsonify(data=serialized_roles), 200


@role_routes.route('/roles/users', methods=['GET'])
@jwt_required()
def users():
    users_list = User.query.all()
    user_schema = UserSchema(many=True)  # Use many=True for lists
    serialized_users = user_schema.dump(users_list)
    return jsonify(data=serialized_users), 200
