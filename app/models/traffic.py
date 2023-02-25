from sqlalchemy import DateTime
from sqlalchemy.sql import func
from app.extensions import db

class Traffic(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  srcIp = db.Column(db.String(80))
  dstIp = db.Column(db.String(80))
  status = db.Column(db.String(10))
  createdAt = db.Column(DateTime(timezone=True), server_default=func.now())
  updatedAt = db.Column(DateTime(timezone=True), onupdate=func.now())

  def __init__(self, srcIp, dstIp, status):
    self.srcIp = srcIp
    self.dstIp = dstIp
    self.status = status

  def serialize(self):
    return {
      "srcIp": self.srcIp,
      "dstIp": self.dstIp,
      "status": self.status,
    }