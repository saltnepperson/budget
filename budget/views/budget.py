import datetime
from flask import request, jsonify
from flask_restful import reqparse, marshal_with, Resource

from budget.models.budget import Budget, BudgetSchema
from budget.views import BUDGET_FIELDS

# List all of the users
class BudgetPostList(Resource):

    def __init__(self):
        self.reqparse = reqparse
    
    @marshal_with(BUDGET_FIELDS, envelope='budgets')
    def get(self):
        # Additional request arguments
        parser = self.reqparse.RequestParser()
        
        parser.add_argument('count', type=int, default=30, location='args')
        parser.add_argument('page', type=int, default=1, location='args')

        args = parser.parse_args()

        query = Budget.query

        results = query.paginate(args.page, args.count)

        return results.items, 200
    
    @marshal_with(BUDGET_FIELDS, envelope='user')
    def post(self):

        schema = BudgetSchema()
        args = schema.load(request.get_json())

        # Budget create fields
        budget = Budget(
            name=args.get('name'),
            description=args.get('description'),
            type=args.get('type'),
            created_by=args.get('created_by'),
            created_at=datetime.datetime.utcnow
        )

        result = schema.dump(budget.create())

        return result, 201

class BudgetGetPutDelete(Resource):

    @marshal_with(BUDGET_FIELDS, envelope='budget')
    def get(self, id):
        
        budget = Budget.query.get_or_404(id)

        return budget, 200

    @marshal_with(BUDGET_FIELDS, envelope='budget')
    def put(self, id):

        schema = BudgetSchema()
        args = schema.load(request.get_json())

        budget_to_update = Budget.query.get(id)

        # Update those fields!
        if args.get('name'):
            budget_to_update.name = args.get('name')
        if args.get('description'):
            budget_to_update.description = args.get('description')
        if args.get('type'):
            budget_to_update.type = args.get('type')
        
        budget_to_update.updated_at = datetime.datetime.utcnow

        budget = schema.dump(budget_to_update.update())

        return budget, 204
    
    def delete(self, id):

        budget_to_delete = Budget.query.get_or_404(id)

        budget_to_delete.delete()

        return 204