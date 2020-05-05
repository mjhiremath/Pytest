import requests
import pytest
import json

@pytest.mark.user
def test_user_API(supply_url):
    url = supply_url+"/user"
    response = requests.get(url,headers={'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'})
    json1 = response.json()
    j = json.loads(response.text)
    assert response.url == 'https://api.github.com/user'
    assert json1['login'] == 'mjhiremath'
    assert response.status_code == 200