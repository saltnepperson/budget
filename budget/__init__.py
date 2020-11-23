import os
import stat
import boto3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from os.path import dirname, join, isfile
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
client = boto3.client('kinesis', endpoint_url='http://localhost:4566')

configFile = dirname(dirname(__file__))
configFile = join(configFile, 'config')
configFile = join(configFile, '{}-config.py'.format(os.getenv('ENV')))

if isfile(configFile):
    print('Loading config - {}-config.py'.format(os.getenv('ENV')))
    app.config.from_pyfile(configFile)
else:
    print('A config file is required: {}-config.py'.format(os.getenv('ENV')))
    exit(-1)

# This is where we intialize extensions that rely on the app
db.init_app(app)
migrate.init_app(app, db)

# Add stream to Kinesis if present, if not, create it and add a stream
streams = client.list_streams()

if 'budget' not in streams['StreamNames']:
    client.create_stream(
        StreamName='budget',
        ShardCount=1
    )

### Flask API ###
from flask_restful import Api
api = Api(app)

from budget.views.user import UserPostList
from budget.views.user import UserGetPutDelete
api.add_resource(UserPostList, '/api/users')
api.add_resource(UserGetPutDelete, '/api/users/<int:id>')

from budget.views.budget import BudgetPostList
from budget.views.budget import BudgetGetPutDelete
api.add_resource(BudgetPostList, '/api/budgets')
api.add_resource(BudgetGetPutDelete, '/api/budgets/<int:id>')

from budget.views.budget_item import BudgetItemPostList
from budget.views.budget_item import BudgetItemGetPutDelete
api.add_resource(BudgetItemPostList, '/api/budget_items')
api.add_resource(BudgetItemGetPutDelete, '/api/budget_items/<int:id>')