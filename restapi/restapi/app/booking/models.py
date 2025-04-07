from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, connect
from datetime import datetime

# Connect to MongoDB
connect('ticket_booking_db')

class Ticket(Document):
    title = StringField(required=True)
    description = StringField()
    price = IntField(required=True)
    available_quantity = IntField(required=True)
    event_date = DateTimeField(required=True)
    is_active = BooleanField(default=True)

    meta = {
        'collection': 'tickets'
    }

    def book_ticket(self, quantity):
        if self.available_quantity >= quantity:
            self.available_quantity -= quantity
            self.save()
            return True
        return False

    def __str__(self):
        return f'Ticket({self.title}, {self.available_quantity} available)'