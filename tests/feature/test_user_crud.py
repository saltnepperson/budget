import pytest

class TestUserCrud:

    def test_user_get(self, api_client, test_user):
        response = api_client.get('/api/users/{}'.format(test_user.id))
        data = response.get_json()
        assert data['user']['first_name'] == test_user.first_name
        assert data['user']['last_name'] == test_user.last_name
        assert data['user']['email'] == test_user.email

    def test_user_list(self, api_client, test_user):
        response = api_client.get('/api/users')
        data = response.get_json()
        assert data['users'][0]['first_name'] is not None
        assert data['users'][0]['first_name'] == test_user.first_name
        assert data['users'][0]['last_name'] == test_user.last_name
        assert data['users'][0]['email'] == test_user.email

    def test_user_update(self, api_client, test_user):
        response = api_client.put('/api/users/{}'.format(test_user.id), json={
            'first_name': 'updated',
            'last_name': 'test',
            'email': 'something@gmail.com'
        })

        assert response.status_code == 204

