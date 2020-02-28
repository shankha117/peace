from tests import client
import json

url = '/peace/v1/api/users'

Post_mock_request_headers = {
    'Content-Type': 'application/json'
}

mock_request_data = {
    "id": 123399998,
    "first_name": "fn2",
    "last_name": "ln3",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 89
}
mock_request_without_id = {
    "first_name": "fn2",
    "last_name": "ln3",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 89
}


def test_create_user_pass(client):
    response = client.post(url, json=mock_request_data, headers=Post_mock_request_headers)
    assert response.status_code == 201


def test_create_user_fail(client):
    response = client.post(url, json=mock_request_data, headers=Post_mock_request_headers)
    assert response.get_data() == b'{\n  "message": "id -  123399998 already exists"\n}\n'
    assert response.status_code == 500


def test_create_user_without_id(client):
    response = client.post(url, json=mock_request_without_id, headers=Post_mock_request_headers)
    assert json.loads(response.get_data()) == {"message": "the key ``id`` is required"}
    assert response.status_code == 400
