from flask import jsonify, request
import random

from app.extensions import db
from app.traffics import bp
from app.models.traffic import Traffic

@bp.route("/api/traffics", methods=["GET"])
def get_all_traffics():
  traffics = Traffic.query.all()
  return jsonify([ traffic.serialize() for traffic in traffics ])


@bp.route("/api/traffics", methods=["POST"])
def create_traffic():
  amount = request.form["amount"]
  res = []

  for _ in range(int(amount)):
    srcIp = request.remote_addr

    # model to classified status here
    status = random.choices(["anomaly", "normal"])[0]

    traffic = Traffic(srcIp, status)

    db.session.add(traffic)
    db.session.commit()
    res.append(traffic)

  res = [ r.serialize() for r in res ]
  return jsonify({ "response": res })