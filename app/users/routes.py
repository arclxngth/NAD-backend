from flask import jsonify, request

from app.extensions import db
from app.users import bp
from app.models.user import User

@bp.route("/api/users", methods=["GET", "POST"])
def create():
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    user = User(username, password)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201