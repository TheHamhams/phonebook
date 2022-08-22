import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
        Set config variables for the flask app
        using Environment variables where available.
        Otherwise, create the config variable if not done already
    '''
    
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_RUN = os.getenv('FLASK_RUN')
    SECRET_KEY = os.environ.get('SECRET KEY') or 'placehodler string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
