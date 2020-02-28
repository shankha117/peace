from tests import client
import json


url = '/peace/v1/api/users/'

Post_mock_request_headers = {
    'Content-Type': 'application/json'
}

available_user_id = '123399999'
unavailable_user_id = '30000'

mock_response = {
    "id": 123399999,
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


def test_get_user_pass(client):
    response = client.get(url+str(available_user_id))
    assert json.loads(response.get_data()) == mock_response
    assert response.status_code == 200

def test_get_user_fail(client):
    response = client.get(url+str(unavailable_user_id))
    assert json.loads(response.get_data()) == {"message": "no users found"}
    assert response.status_code == 200


