from flask import jsonify, request
import linecache
import random

from app.extensions import db
from app.traffics import bp
from app.models.traffic import Traffic
from app.traffics.service import nad_predict

nLine = len(linecache.getlines("app/common/dataset"))

@bp.route("/api/traffics", methods=["GET"])
def get_all_traffics():
  traffics = Traffic.query.all()
  return jsonify([ traffic.serialize() for traffic in traffics ])

@bp.route("/api/traffics", methods=["POST"])
def create_traffic():
  res = []
  amount = int(request.form["amount"])

  idx_lists = random.sample(range(2, nLine), amount)

  for idx in idx_lists:
    # preparing feature
    datas = linecache.getline("app/common/dataset", idx)
    features = datas.split(",")[:-1]
    features = [[ float(f) for f in features ]]

    # predict
    status = nad_predict(features)
    srcIp = request.remote_addr

    traffic = Traffic(srcIp, status)

    db.session.add(traffic)
    db.session.commit()
    res.append(traffic)

  res = [ r.serialize() for r in res ]
  return jsonify({ "response": res })