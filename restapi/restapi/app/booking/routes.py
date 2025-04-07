from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from app.booking.services import search_tickets, book_ticket, check_booking_status
from flask_jwt_extended import jwt_required

booking_bp = Blueprint('booking', __name__)
mongo = PyMongo()

@booking_bp.route('/tickets/search', methods=['GET'])
def search():
    query_params = request.args
    tickets = search_tickets(query_params)
    return jsonify(tickets), 200

@booking_bp.route('/tickets/book', methods=['POST'])
@jwt_required()
def book():
    data = request.json
    result = book_ticket(data)
    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@booking_bp.route('/tickets/status/<booking_id>', methods=['GET'])
@jwt_required()
def status(booking_id):
    status = check_booking_status(booking_id)
    return jsonify(status), 200