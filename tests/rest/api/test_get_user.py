from tests import client
import json


url = '/peace/v1/api/users/'

Post_mock_request_headers = {
    'Content-Type': 'application/json'
}

available_user_id = '2'
unavailable_user_id = '10231'

mock_response = {
    "age": 48,
    "city": "Brighton",
    "company_name": "Chanay, Jeffrey A Esq",
    "email": "josephine_darakjy@darakjy.org",
    "first_name": "Josephine",
    "id": 2,
    "last_name": "Darakjy",
    "state": "MI",
    "web": "http://www.chanayjeffreyaesq.com",
    "zip": 48116
}


def test_get_user_pass(client):
    response = client.get(url+str(available_user_id))
    assert json.loads(response.get_data()) == mock_response
    assert response.status_code == 200

def test_get_user_fail(client):
    response = client.get(url+str(unavailable_user_id))
    assert json.loads(response.get_data()) == {"message": "no users found"}
    assert response.status_code == 200


