from sqlalchemy import Column, Integer, String, DateTime, Boolean, Unicode, Text
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from budget import app, db
from budget.models.users import User

# The budget model stores all of a users budgets
class Budget(db.Model):
    """
    Represents a budget app user's budget.
    """
    __tablename__ = 'budgets'

    # Basic user info
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    # This can be expanded upon as it's own model
    # i.e. "Monthly Budget", "House Repairs", etc.
    type = db.Column(db.String(50))

    # Relationships
    created_by = db.Column(
        db.Integer,
        db.ForeignKey(User.id, ondelete='CASCADE'),
        nullable=False
    )
    
    # timestamps
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name, created_by, description=None, type=None, created_at=None, updated_at=None):
        self.name = name
        self.description = description
        self.type = type
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return '<%s>' % self

    # TODO: move into a parent model class as it's shared functionality
    def create(self):
        db.session.add(self)
        db.session.commit()

        return self

    def update(self):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        return self

class BudgetSchema(Schema):

    class Meta(Schema.Meta):
        model = Budget
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    type = fields.String()
    created_by = fields.Number()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
