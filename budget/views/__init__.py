from flask_restful import fields

USER_FIELDS = {
    'id': fields.Integer,
    'first_name': fields.String,
    'middle_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'username': fields.String
}