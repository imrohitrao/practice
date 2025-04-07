# This file initializes the booking module and registers its routes with the main application.

from flask import Blueprint

booking_bp = Blueprint('booking', __name__)

from . import routes  # Import routes to register them with the blueprint