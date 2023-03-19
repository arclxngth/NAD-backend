import uuid
from flask_bcrypt import Bcrypt
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from app.extensions import db
from flask_login import UserMixin

bcrypt = Bcrypt()

class User(UserMixin, db.Model):
  id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  createdAt = db.Column(DateTime(timezone=True), server_default=func.now())
  updatedAt = db.Column(DateTime(timezone=True), onupdate=func.now())

  def __init__(self, username, password):
    self.username = username
    self.password = bcrypt.generate_password_hash(password).decode('utf-8')

  def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)

  def serialize(self):
    return {
      "id": self.id,
      "username": self.username,
    }