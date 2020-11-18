import os
import stat

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, join, isfile

app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

# Get that environment configuration
configFile = dirname(dirname(__file__))
configFile = join(configFile, 'env-config')

if (app.env == 'testing'):
    configFile = join(configFile, 'test-config.py')
else:
    configFile = join(configFile, 'config.py')

if isfile(configFile):
    app.config.from_pyfile(configFile)
else:
    print('We need a config file to run this application.')
    exit(-1)

### Flask API ###
from flask_restful import Api
api = Api(app)

from budget.views.user import UserPostList
from budget.views.user import UserGetPutDelete
api.add_resource(UserPostList, '/api/users')
api.add_resource(UserGetPutDelete, '/api/users/<int:id>')