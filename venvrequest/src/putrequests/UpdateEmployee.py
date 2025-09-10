import requests
import json
file=open("venvrequest/payloads/update.json","r")
input=file.read()
payload=json.loads(input)
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
response=requests.put("https://dummy.restapiexample.com/api/v1/update/8577",data=payload,headers=headers)
data=response.json
def test_StatusCode():
    assert response.status_code==200
def test_ContentType(): 
    assert response.headers["Content-Type"]=="application/json"
def test_ContentEncoding():
    assert response.headers["Content-Encoding"]=="gzip"
def test_StatusLine():
    assert response.ok
def test_SuccessCode():
    assert data()["message"]=="Successfully! Record has been updated."
def test_CreateEmployeeSuccessfull():
    assert data()["status"]=="success"