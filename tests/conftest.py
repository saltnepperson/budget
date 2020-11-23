import os
import tempfile

import pytest

from unittest import mock
from budget import app, db
from budget.models.users import User
from budget.models.budget import Budget
from budget.models.budget_item import BudgetItem

@pytest.fixture(scope='module')
def api_client():
    flask_app = app

    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client

# Create a test user for us to work with
@pytest.fixture(scope='module')
def test_user(api_client):
    db.create_all()

    user = User(first_name='testy', last_name='test', email='testme@gmail.com', username='testing', password='testpass')

    db.session.add(user)
    db.session.commit()

    yield user

    db.session.delete(user)
    db.session.commit()

# Create a budget to test with
@pytest.fixture(scope='module')
def test_budget(api_client, test_user):
    budget = Budget(name='Test Budget', description='Test test test test.', category='Test', created_by=test_user.id)

    db.session.add(budget)
    db.session.commit()

    yield budget

    db.session.delete(budget)
    db.session.commit()

# Create a budget item to test with
@pytest.fixture(scope='module')
def test_budget_item(api_client, test_user, test_budget):
    budget_item = BudgetItem(name='Test Budget Item', description='Test test test test.', category='Test Item', created_by=test_user.id, budget_id=test_budget.id)

    db.session.add(budget_item)
    db.session.commit()

    yield budget

    db.session.delete(budget_item)
    db.session.commit()