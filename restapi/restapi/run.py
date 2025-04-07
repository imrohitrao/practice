from flask import Flask
from app.database.connection import init_db
from app.auth.routes import auth_bp
from app.booking.routes import booking_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    init_db(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(booking_bp, url_prefix='/booking')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)