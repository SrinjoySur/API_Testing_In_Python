import requests
def GetPostsById():
    baseUri="https://jsonplaceholder.typicode.com"
    response=requests.get(baseUri+"/posts/1")
    assert response.ok
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    data =response.json()
    assert isinstance(data,dict)
    assert "id" in data
    assert "title" in data
    assert "body" in data
    
GetPostsById()