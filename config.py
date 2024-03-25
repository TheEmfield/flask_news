import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATDABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False