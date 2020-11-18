ENVIRONMENT = 'development'

# Database configuration
DATABASE_HOST = 'postgresql'
DATABASE_URL = 'localhost'
DATABASE_PORT = 5432
DATABASE_DB = 'budget_dev'
DATABASE_PASSWORD = 'thisisasecurepassword'
DATABASE_USER = 'budget_user'

SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    DATABASE_HOST,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_DB
)

# Api configuration
API_PORT = 5000
API_HOST = 'localhost'
API_PATH = '/api/'

BASE_URL = 'http://{}:{}{}'.format(API_HOST, API_PORT, API_PATH)

DEBUG = True
