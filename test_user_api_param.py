import pytest
import requests

@pytest.mark.param
@pytest.mark.parametrize("id,login",[(60935194,"mjhiremath")])
def test_user_API(supply_url,id,login):
    url = supply_url + "/users/"+login
    headers = {'content-type': 'application/json'}
    response = requests.get(url,headers={'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'})
    result = response.json()
    assert response.status_code == 200, response.text
    assert result['id'] == id, response.text
    assert result['login'] == login, response.text
    assert result['plan']['name'] == 'free'

@pytest.mark.param
def test_invalid_credentials(supply_url):
    url = supply_url + "/user/"
    response = requests.get(url,headers={'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'})
    assert response.status_code == 404

@pytest.mark.run
def test_post_gist(supply_url):
    url = supply_url +"/gists"
    headers = {'Authorization':'Bearer bfcc743ee4211976c82734b074d15b51383e5277'}
    #json_payload = {"description": "Hello World Examples","files": {"hello_world_ruby.txt": {"content": "Run `ruby hello_world.rb` or `python hello_world.py` to print Hello World","filename": "hello_world.md"},"new_file.txt": {"content": "This is a new placeholder file."}}}
    json_payload = {
      "description": "Hello World Examples",
      "files": {
        "hello_world_ruby.txt": {
          "content": "Run `ruby hello_world.rb` or `python hello_world.py` to print Hello World",
          "filename": "hello_world.md"
        },
        "new_file.txt": {
          "content": "This is a new placeholder file."
        }
      }
    }
    response = requests.post(url,json=json_payload,headers=headers)
    assert response.status_code == 201

@pytest.mark.delete
@pytest.mark.parametrize("id",('9cd6b8576aa2aab754d6b4e439dfc425'))
def test_delete_gist(supply_url,id):
    url = supply_url+"/gists/"+id
    headers = {'Authorization': 'Bearer bfcc743ee4211976c82734b074d15b51383e5277'}
    response = requests.delete(url,headers=headers)
    j = response.json()
    assert response.status_code == 204
    assert j[id] == id, response.text