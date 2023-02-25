from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from app.auth import bp
from app.models.user import User


@bp.route("/api/login", methods=["POST"])
def login():
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]

    if not username or not password:
      return jsonify({"message": "username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid username or password"}), 401
  
    token = create_access_token(identity=user.id)

    return jsonify({ "token": token }), 200
  
@bp.route('/api/me', methods=['GET'])
@jwt_required()
def me():
  user_id = get_jwt_identity()
  user = User.query.get(user_id)
  return jsonify(user.serialize()), 200