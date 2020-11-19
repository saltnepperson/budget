import os
import tempfile

import pytest

from budget import create_app, db
from budget.models.users import User

@pytest.fixture(scope='module')
def api_client():
    flask_app = create_app('test-config.py')

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