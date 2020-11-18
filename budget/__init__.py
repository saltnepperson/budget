import os
import stat

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, join, isfile

app = Flask(__name__)
db = SQLAlchemy()

# Get that environment configuration
configFile = dirname(dirname(__file__))
configFile = join(configFile, 'env-config')
configFile = join(configFile, 'config.py')

if isfile(configFile):
    app.config.from_pyfile(configFile)
else:
    print('We need a config file to run this application.')
    exit(-1)

### Flask API ###
from flask_restful import Api
api = Api(app)

from budget.views.user import UserList
api.add_resource(UserList, '/api/users')