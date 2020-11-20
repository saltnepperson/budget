# Test environment configuration
ENVIRONMENT = 'testing'

# Database configuration
DATABASE_HOST = 'postgresql'
DATABASE_URL = 'localhost'
DATABASE_PORT = 5432
DATABASE_DB = 'budget_test'
DATABASE_PASSWORD = 'thisisasecurepassword'
DATABASE_USER = 'budget_user'

SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Api configuration
API_PORT = 5000
API_HOST = 'localhost'
API_PATH = '/api/'

BASE_URL = 'http://{}:{}{}'.format(API_HOST, API_PORT, API_PATH)

DEBUG = True
