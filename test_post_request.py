import requests
import pytest

def test_post_request(post_url):
    jsonPayload = {'albumId':1,'title':'test','url':'hiremath.com','thumbnailUrl':'hiremath.com','id':5001}
    url = post_url+'/photos'
    headers = {'content-type': 'application/json'}
    response = requests.post(url,json=jsonPayload,headers=headers)
    assert response.status_code == 201