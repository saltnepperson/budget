ENVIRONMENT = 'local'

# Database configuration
SQLALCHEMY_DATABASE_URI = 'postgresql://budget_user:thisisasecurepassword@localhost:5432/budget_dev'

# Api configuration
API_PORT = 5000
API_HOST = 'localhost'
API_PATH = '/api/'

BASE_URL = 'http://{}:{}{}'.format(API_HOST, API_PORT, API_PATH)

DEBUG = True
