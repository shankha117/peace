from tests import client
import json

url = '/peace/v1/api/users'

Post_mock_request_headers = {
    'Content-Type': 'application/json'
}


def test_get_all_users_with_no_page(client):
    response = client.get(url)
    assert json.loads(response.get_data()) == {"message": "the key ``page`` is required"}
    assert response.status_code == 400


def test_get_user_with_normal_limit(client):
    response = client.get(url + "?page=1")
    assert len(json.loads(response.get_data())['data']) == 5
    assert response.status_code == 200


def test_get_user_with_limit_10(client):
    response = client.get(url + "?limit=10&page=1")
    assert len(json.loads(response.get_data())['data']) == 10
    assert response.status_code == 200
