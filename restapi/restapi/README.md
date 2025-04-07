# Ticket Booking System API

This project is a Flask REST API for a ticket booking system that integrates with MongoDB. It includes user authentication and authorization using JWT tokens, and it is designed to handle concurrency and inventory management effectively.

## Project Structure

```
restapi
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── jwt_handler.py
│   │   └── routes.py
│   ├── booking
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── services.py
│   ├── database
│   │   ├── __init__.py
│   │   └── connection.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── venv/
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd restapi
   ```

2. **Create a virtual environment**:
   ```
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

5. **Configure the application**:
   Update the `config.py` file with your MongoDB connection details and JWT secret key.

6. **Run the application**:
   ```
   python run.py
   ```

## API Usage

- **Authentication**:
  - Register a new user: `POST /auth/register`
  - Login: `POST /auth/login`

- **Booking**:
  - Search available tickets: `GET /booking/tickets`
  - Book a ticket: `POST /booking/tickets/book`
  - Check booking status: `GET /booking/tickets/status`

## Concurrency Management

To maintain consistency and prevent race conditions in the ticket booking system, the following strategies are implemented:

1. **Database Transactions**: Ensures atomic operations for ticket availability checks and bookings.
2. **Optimistic Locking**: Checks ticket inventory before processing a booking to prevent stale data.
3. **Atomic Operations**: Uses MongoDB's atomic operations to modify ticket counts safely.
4. **Queueing Requests**: Handles incoming booking requests sequentially for specific tickets.
5. **Rate Limiting**: Applies limits to booking requests to prevent system overload.

This project aims to provide a robust and scalable solution for ticket booking while ensuring data integrity and user security.