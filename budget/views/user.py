from flask import request
from flask_restful import reqparse, marshal_with, Resource

from budget.models.users import User
from budget.views import USER_FIELDS

# List all of the users
class UserList(Resource):

    def __init__(self):
        self.reqparse = reqparse
    
    @marshal_with(USER_FIELDS)
    def get(self):
        # Additional request arguments
        parser = self.reqparse.RequestParser()
        
        parser.add_argument('count', type=int, default=30, location='args')
        parser.add_argument('page', type=int, default=1, location='args')

        args = parser.args

        query = User.query

        results = query.paginate(args.page, args.count)

        get_return = {
            "users": [results.items]
        }

        return get_return, 200