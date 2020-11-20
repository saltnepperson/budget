import datetime
from flask import request, jsonify
from flask_restful import reqparse, marshal_with, Resource

from budget.models.budget_item import BudgetItem, BudgetItemSchema
from budget.views import BUDGET_ITEM_FIELDS

class BudgetItemPostList(Resource):

    def __init__(self):
        self.reqparse = reqparse
    
    @marshal_with(BUDGET_ITEM_FIELDS, envelope='budget_items')
    def get(self):
        # Additional request arguments
        parser = self.reqparse.RequestParser()
        
        parser.add_argument('count', type=int, default=30, location='args')
        parser.add_argument('page', type=int, default=1, location='args')

        args = parser.parse_args()

        query = BudgetItem.query

        results = query.paginate(args.page, args.count)

        return results.items, 200
    
    @marshal_with(BUDGET_ITEM_FIELDS, envelope='budget_item')
    def post(self):

        schema = BudgetItemSchema()
        args = schema.load(request.get_json())

        # Budget Item create fields
        budget_item = BudgetItem(
            name=args.get('name'),
            description=args.get('description'),
            category=args.get('category'),
            budget_id=args.get('budget_id'),
            created_by=args.get('created_by')
        )

        result = schema.dump(budget_item.create())

        return result, 201

class BudgetItemGetPutDelete(Resource):

    @marshal_with(BUDGET_ITEM_FIELDS, envelope='budget_item')
    def get(self, id):
        
        budget = BudgetItem.query.get_or_404(id)

        return budget, 200

    @marshal_with(BUDGET_ITEM_FIELDS, envelope='budget_item')
    def put(self, id):

        schema = BudgetItemSchema()
        args = schema.load(request.get_json())

        budget_item_to_update = BudgetItem.query.get(id)

        # Update those fields!
        if args.get('name'):
            budget_item_to_update.name = args.get('name')
        if args.get('description'):
            budget_item_to_update.description = args.get('description')
        if args.get('category'):
            budget_item_to_update.category = args.get('category')
        
        budget_item_to_update.updated_at = datetime.datetime.utcnow()

        budget_item = schema.dump(budget_item_to_update.update())

        return budget_item, 204
    
    def delete(self, id):

        budget_item_to_delete = BudgetItem.query.get_or_404(id)

        budget_item_to_delete.delete()

        return budget_item_to_delete, 204