from flask import abort, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.user import User

@jwt_required()
def validate_user():
  user_id = get_jwt_identity()
  user = User.query.get(user_id)
  if user is None:
    abort(404, "user not found")  

  return jsonify(user.serialize()), 200