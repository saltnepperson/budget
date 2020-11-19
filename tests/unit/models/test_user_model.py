from budget.models.users import User

def test_new_user():
    user = User(
        first_name='testing',
        last_name='tester',
        email='teststesttest@gmail.com',
        username='TestMe11',
        password='Thisisatestpass'
    )
    assert user.email == 'teststesttest@gmail.com'
    assert user.username == 'TestMe11'

def test_new_user_with_fixture(test_user):
    assert test_user.email == 'testme@gmail.com'
