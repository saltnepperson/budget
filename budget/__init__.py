import os
import stat

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, join, isfile

db = SQLAlchemy()

# Get that environment configuration
def create_app(config_file=None):
    app = Flask(__name__)

    if config_file is None:
        config_file = 'config.py'

    configFile = dirname(dirname(__file__))
    configFile = join(configFile, 'env-config')
    configFile = join(configFile, config_file)

    if isfile(configFile):
        app.config.from_pyfile(configFile)
    else:
        print('We need a config file to run this application.')
        exit(-1)

    initialize_extensions(app)
    register_resources(app)

    return app

# This is where we intialize extensions that rely on the app
def initialize_extensions(app):
    db.init_app(app)


### Flask API ###
def register_resources(app):
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