from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from config import Config
from app.extensions import db

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  # Initialize Flask extensions
  db.init_app(app)

  migrate = Migrate(app, db, render_as_batch=False)

  jwt = JWTManager(app)

  # Register blueprints
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  from app.users import bp as user_bp
  app.register_blueprint(user_bp)

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp)

  from app.traffics import bp as traffic_bp
  app.register_blueprint(traffic_bp)
  
  @app.route('/test')
  def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'

  return app