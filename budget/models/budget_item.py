import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Unicode, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from marshmallow import Schema, fields
from budget import db
from budget.models.budget import BudgetSchema

# The BudgetItem model stores ledger item data for each budget
class BudgetItem(db.Model):
    """
    Represents a budget item.
    """
    __tablename__ = 'budget_items'

    # Basic info
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    # This represents a ledger amount (12.45) or 12.45
    # Think in accounting terms
    # This value will be used to determine if the user is going over budget
    amount = db.Column(db.Integer)

    # This can be expanded upon as it's own model
    # i.e. "Monthly Budget", "House Repairs", etc.
    category = db.Column(db.String(50))

    # Relationships
    budget_id = db.Column(db.Integer, db.ForeignKey('budgets.id'), nullable=False)
    

    # User that created the item, open for collaboration if 
    # multiple users want to work on the same budget
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    
    # timestamps
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    def __init__(self, name, budget_id, created_by, amount=0, description=None, category=None, created_at=None, updated_at=None):
        self.name = name
        self.description = description
        self.category = category
        self.amount = amount
        self.budget_id = budget_id
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

class BudgetItemSchema(Schema):

    class Meta(Schema.Meta):
        model = BudgetItem
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    category = fields.String()
    budget_id = fields.Nested(BudgetSchema, only=['name', 'amount','id'])
    created_by = fields.Number()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
