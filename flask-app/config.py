import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'modzy modelops are incredible'

	API_URL = os.environ.get('API_URL') or "https://demo.modzy.engineering"
	API_KEY = os.environ.get('API_KEY') or "API_KEY_Public.API_KEY_Private"
	
	DEBUG =  os.environ.get('FLASK_DEBUG') or 0