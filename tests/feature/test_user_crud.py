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
        assert data['users'] is not None
        assert len(data['users']) > 0

    def test_user_get_by_id(self, api_client, test_user):
        response = api_client.get('/api/users/{}'.format(test_user.id))
        data = response.get_json()
        assert data['user']['first_name'] == test_user.first_name
        assert data['user']['id'] == test_user.id

    def test_user_update(self, api_client, test_user):
        response = api_client.put('/api/users/{}'.format(test_user.id), json={
            'first_name': 'updated',
            'last_name': 'test',
            'email': 'something@gmail.com'
        })

        assert response.status_code == 204
    
    def test_user_create_and_delete(self, api_client):
        response = api_client.post('/api/users', json={
            "first_name": "User",
            "middle_name": "Create",
            "last_name": "Test",
            "email": "create.user@gmail.com",
            "username": "createuser",
            "password": "thisisapassword"
        })
        data = response.get_json()
        
        assert response.status_code == 201

        response = api_client.delete('/api/users/{}'.format(data['user']['id']))

        assert response.status_code == 204

    def test_user_list_filter_by_first_name(self, api_client, test_user):
        response = api_client.get('/api/users?first_name={}'.format(test_user.first_name))
        data = response.get_json()
        assert data['users'] is not None
        assert data['users'][0]['first_name'] == test_user.first_name
        assert data['users'][0]['id'] == test_user.id