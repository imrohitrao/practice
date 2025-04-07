from flask import Flask
from flask_pymongo import PyMongo
from app.auth.routes import auth_bp
from app.booking.routes import booking_bp
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(booking_bp, url_prefix='/booking')

    return app