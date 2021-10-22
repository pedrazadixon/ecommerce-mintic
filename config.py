import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.urandom(32)
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
