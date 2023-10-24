import os

class Settings:
    DATABASE_HOST = os.environ.get('HOST')
    DATABASE_NAME = os.environ.get('DATABASE')
    DATABASE_USER = os.environ.get('USER')
    DATABASE_PASSWORD = os.environ.get('PASSWORD')
    
settings = Settings()
