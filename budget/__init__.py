import os
import stat

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

# Get that environment configuration
if os.environ.get('BUDGET_SETTINGS'):
    app.config.from_envvar('BUDGET_SETTINGS')
else:
    from os.path import dirname, join, isfile
    configFile = dirname(dirname(__file__))
    configFile = join(configFile, 'env-config')
    configFile = join(configFile, 'config.py')

    print(configFile)

    if isfile(configFile):
        app.config.from_pyfile(configFile)
    else:
        print('We need a config file to run this application')
        exit(-1)

### Flask API ###
from flask_restful import Api
api = Api(app)
