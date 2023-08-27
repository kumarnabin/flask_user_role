from flask import Blueprint
from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token

from config import db
from models import User, Role
from serializers import user_serializer

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already taken'}), 400

    new_user = User(username=username,email=email)
    new_user.set_password(password)
    role = Role.query.filter_by(name='user').first()
    new_user.roles.append(role)
    db.session.commit()
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


@auth_routes.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@auth_routes.route('/auth/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()

    if user:
        serialized_user = user_serializer(user)
        return jsonify(user=serialized_user), 200
    else:
        return jsonify(message='User not found'), 404


@auth_routes.route('/auth/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)
