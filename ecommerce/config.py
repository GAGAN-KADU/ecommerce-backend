import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'm7pMzO3EMuh-adFYzV79RZg3J4zDRQD_iVNMFEfjtCk=')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

