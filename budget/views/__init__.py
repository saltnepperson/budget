from flask_restful import fields

# List of models fields used by marshal for formatting

USER_FIELDS = {
    'id': fields.Integer,
    'first_name': fields.String,
    'middle_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'username': fields.String
}

BUDGET_FIELDS = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'type': fields.String,
    'created_by': fields.Integer
}