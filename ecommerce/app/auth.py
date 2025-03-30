import jwt
import datetime
from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from functools import wraps
import logging

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = Config.SECRET_KEY

def generate_jwt_token(username):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    logging.info(f"Token will expire at {expiration_time}")
    payload = {
        'user': username,
        'exp': expiration_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def token_wrapper(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            logging.error("Token is missing!")
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = decoded_token['user']
            logging.info(f"Current user: {current_user}")
        except jwt.ExpiredSignatureError:
            logging.error("Token has expired!")
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            logging.error("Invalid token!")
            return jsonify({'message': 'Invalid token!'}), 401

        return f(current_user, *args, **kwargs)

    return token_wrapper

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    logging.info(f"Registering user: {username}")

    if User.query.filter_by(username=username).first():
        logging.error("User already exists")
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(password, method='sha256')

    try:
        user = User(username = username, password = hashed_password)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        return jsonify({'msg': 'Please check all the provided details and try again.'}), 500

    return jsonify({'message': 'User created successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        token = generate_jwt_token(username)
        return jsonify({'access_token': token}), 200

    logging.error("Invalid credentials")
    return jsonify({'message': 'Invalid credentials'}), 401


@auth_bp.route('/profile', methods=['GET'])
@token_required
def profile(current_user):
    user = User.query.filter_by(username=current_user).first()
    if user:
        logging.info(f"User found: {user.username}")
        return jsonify({
            'username': user.username,
            'message': 'This is your profile!'
        }), 200

    logging.error("User not found")
    return jsonify({'message': 'User not found'}), 404

