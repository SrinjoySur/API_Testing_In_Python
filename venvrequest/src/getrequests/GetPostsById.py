import requests
import pytest
@pytest.mark.parametrize("header",[
    "application/json; charset=utf-8"
])
def test_GetPostsById(header):
    baseUri="https://jsonplaceholder.typicode.com"
    response=requests.get(baseUri+"/posts/1")
    assert response.ok
    assert response.headers["Content-Type"] == header
    data =response.json()
    assert isinstance(data,dict)
    assert "id" in data
    assert "title" in data
    assert "body" in data
     
