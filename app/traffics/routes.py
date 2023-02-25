from flask import jsonify, request

from app.extensions import db
from app.traffics import bp
from app.models.traffic import Traffic

@bp.route("/api/traffics", methods=["GET"])
def get_all_traffics():
  traffics = Traffic.query.all()
  return jsonify([ traffic.serialize() for traffic in traffics ])


@bp.route("/api/traffics", methods=["POST"])
def create_traffic():
  srcIp = request.form["srcIp"]
  dstIp = request.form["dstIp"]
  status = request.form["status"]

  traffic = Traffic(srcIp, dstIp, status)

  db.session.add(traffic)
  db.session.commit()

  return jsonify(traffic.serialize()), 201