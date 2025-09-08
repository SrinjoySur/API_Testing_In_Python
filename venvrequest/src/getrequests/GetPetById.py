import requests
import pytest
baseUri="https://petstore.swagger.io/v2"
@pytest.mark.parametrize("endpoint",[
    "/pet/12345"
])

def test_GetPetById(endpoint):
    accept={"accept":"application/json"}
    response=requests.get(baseUri+endpoint,headers=accept)
    checkStatusCode(response=response)
    checkCategory(response=response)
    checkHeaders(response=response)
    checkName(response=response)
    checkStatus(response=response)

def checkStatusCode(response):
    assert response.ok
    
def checkHeaders(response):
    assert response.headers.get("Content-Type")=="application/json"
def checkCategory(response):
    assert response.json()["category"]["name"] == "dog"
def checkName(response):
    assert response.json()["name"]=="snoopie"
def checkStatus(response):
    assert response.json()["status"]=="pending"
