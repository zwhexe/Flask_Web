import os, sys


class Config:

	WIN = sys.platform.startswith('win')
	if WIN:
	    prefix = 'sqlite:///'
	else:
	    prefix = 'sqlite:////'

	SECRET_KEY = '53931504500502c010c502501d297e5a'
	SQLALCHEMY_DATABASE_URI = prefix+os.path.join(os.getcwd(),'site.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')