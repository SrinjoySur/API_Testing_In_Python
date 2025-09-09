import requests
import pytest
baseUri="https://jsonplaceholder.typicode.com"
@pytest.fixture(params=[
    {"users":"/users"}
])
def endpoints(request):
    return request.param
def test_statusCode(endpoints):
    endpoint=endpoints["users"]
    response=requests.get(baseUri+endpoint)
    assert response.status_code==200
def test_NumberOfUsersGreaterThanThree(endpoints):
    endpoint=endpoints["users"]
    response=requests.get(baseUri+endpoint)
    data=response.json()
    assert len(data) > 3
def test_ErvinHowellInUsersList(endpoints):
    endpoint=endpoints["users"]
    response=requests.get(baseUri+endpoint)
    data=response.json()
    assert any(user.get("name") == "Ervin Howell" for user in data)