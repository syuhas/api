import os


class Config(object):
    DEBUG=True

    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI=os.getenv('DB_URL_MYDB')

class Prod(Config):
    DEBUG=False
