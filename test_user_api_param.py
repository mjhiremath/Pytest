import pytest
import requests

@pytest.mark.param
@pytest.mark.parametrize("id,login",[(60935194,"mjhiremath")])
def test_user_API(supply_url,id,login):
    url = supply_url + "/users/"+login
    response = requests.get(url,headers={'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'})
    result = response.json()
    assert response.status_code == 200, response.text
    assert result['id'] == id, response.text
    assert result['login'] == login, response.text

@pytest.mark.param
def test_invalid_credentials(supply_url):
    url  = supply_url + "/user/"
    response = requests.get(url,headers={'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'})
    assert response.status_code == 404

