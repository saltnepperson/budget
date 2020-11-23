from flask_restful import fields

# List of models fields used by marshal for formatting

USER_FIELDS = {
    'id': fields.Integer,
    'first_name': fields.String,
    'middle_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'username': fields.String,
    'budgets': fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'category': fields.String,
        'amount': fields.Integer
    })
}

BUDGET_FIELDS = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'category': fields.String,
    'created_by': fields.Integer,
    'budget_items': fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'category': fields.String,
        'amount': fields.Integer
    })
}

BUDGET_ITEM_FIELDS = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'category': fields.String,
    'budget_id': fields.Integer,
    'created_by': fields.Integer
}