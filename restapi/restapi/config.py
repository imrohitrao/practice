from flask import Config

class Config:
    SECRET_KEY = 'your_secret_key_here'
    MONGO_URI = 'mongodb://localhost:27017/your_database_name'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = 86400  # 1 day
    DEBUG = True  # Set to False in production
    TESTING = False  # Set to True for testing environment

# Additional configurations can be added as needed.