from tests import client
import json

url = '/peace/v1/api/users'

Post_mock_request_headers = {
    'Content-Type': 'application/json'
}

available_user_id = '10235'
unavailable_user_id = '10231'

def test_delete_user_success(client):
    response = client.delete(url+"/"+available_user_id)
    assert json.loads(response.get_data()) == {"message": "1 user deleted"}
    assert response.status_code == 200


def test_delete_user_fail(client):
    response = client.delete(url + "/"+unavailable_user_id)
    assert json.loads(response.get_data()) == {"error": "no user with the id 10231 exists"}
    assert response.status_code == 400
