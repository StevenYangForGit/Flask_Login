import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Mail Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PROT = 465,
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or 'GMAIL_USERNAME'
    MAIL_USERNAME = os.environ.get('GMAIL_PASSWORD') or 'GMAIL_PASSWORD'