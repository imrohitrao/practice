from flask import current_app
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

mongo = PyMongo()

def reserve_ticket(ticket_id, user_id):
    ticket = mongo.db.tickets.find_one({"_id": ObjectId(ticket_id)})
    
    if not ticket or ticket['available'] <= 0:
        return {"message": "Ticket not available"}, 400

    try:
        result = mongo.db.tickets.find_one_and_update(
            {"_id": ObjectId(ticket_id), "available": {"$gt": 0}},
            {"$inc": {"available": -1}},
            return_document=True
        )
        
        if result is None:
            return {"message": "Ticket not available"}, 400
        
        booking = {
            "ticket_id": ticket_id,
            "user_id": user_id,
            "status": "reserved"
        }
        
        mongo.db.bookings.insert_one(booking)
        return {"message": "Ticket reserved successfully"}, 200

    except DuplicateKeyError:
        return {"message": "Booking already exists"}, 400

def get_ticket_availability(ticket_id):
    ticket = mongo.db.tickets.find_one({"_id": ObjectId(ticket_id)})
    
    if not ticket:
        return {"message": "Ticket not found"}, 404
    
    return {"available": ticket['available']}, 200

def cancel_reservation(booking_id):
    booking = mongo.db.bookings.find_one({"_id": ObjectId(booking_id)})
    
    if not booking:
        return {"message": "Booking not found"}, 404

    ticket_id = booking['ticket_id']
    
    mongo.db.bookings.delete_one({"_id": ObjectId(booking_id)})
    mongo.db.tickets.find_one_and_update(
        {"_id": ObjectId(ticket_id)},
        {"$inc": {"available": 1}}
    )
    
    return {"message": "Reservation cancelled successfully"}, 200