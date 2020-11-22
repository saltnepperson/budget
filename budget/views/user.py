from flask import request, jsonify
from flask_restful import reqparse, marshal_with, Resource

from budget.models.users import User, UserSchema
from budget.views import USER_FIELDS

# List all of the users
class UserPostList(Resource):

    def __init__(self):
        self.reqparse = reqparse
    
    @marshal_with(USER_FIELDS, envelope='users')
    def get(self):
        # Additional request arguments
        parser = self.reqparse.RequestParser()
        
        parser.add_argument('count', type=int, default=30, location='args')
        parser.add_argument('page', type=int, default=1, location='args')

        args = parser.parse_args()

        query = User.query

        results = query.paginate(args.page, args.count)

        return results.items, 200
    
    @marshal_with(USER_FIELDS, envelope='user')
    def post(self):

        data = request.get_json()
        user_schema = UserSchema()
        args = user_schema.load()

        # User create fields
        user = User(
            first_name=args.get('first_name'),
            middle_name=args.get('middle_name'),
            last_name=args.get('last_name'),
            email=args.get('email'),
            username=args.get('username'),
            password=args.get('password')
        )

        result = user_schema.dump(user.create())

        return result, 201

class UserGetPutDelete(Resource):

    @marshal_with(USER_FIELDS, envelope='user')
    def get(self, id):
        
        user = User.query.get_or_404(id)

        return user, 200

    @marshal_with(USER_FIELDS, envelope='user')
    def put(self, id):

        user_schema = UserSchema()
        args = request.get_json(force=True)

        user_to_update = User.query.get(id)

        # Update those fields!
        if args.get('first_name'):
            user_to_update.first_name = args.get('first_name')
        if args.get('middle_name'):
            user_to_update.middle_name = args.get('middle_name')
        if args.get('last_name'):
            user_to_update.last_name = args.get('last_name')
        if args.get('username'):
            user_to_update.username = args.get('username')
        if args.get('email'):
            user_to_update.email = args.get('email')
        if args.get('password'):
            user_to_update.password = args.get('password')

        user = user_schema.dump(user_to_update.update())

        return user, 204
    
    def delete(self, id):

        user_to_delete = User.query.get_or_404(id)

        user_to_delete.delete()

        return {}, 204
