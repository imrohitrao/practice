def validate_input(data):
    # Validate input data for booking requests
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary.")
    
    required_fields = ['user_id', 'ticket_id', 'quantity']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
        raise ValueError("Quantity must be a positive integer.")

    return True

def format_response(status, message, data=None):
    # Format the response for API endpoints
    response = {
        'status': status,
        'message': message
    }
    if data is not None:
        response['data'] = data
    return response

def handle_error(error):
    # Handle errors and format them for the response
    return format_response('error', str(error))