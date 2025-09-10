import requests

appendpoint= "https://dummy.restapiexample.com/api/v1/employees"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
response=requests.get(appendpoint,headers=headers)
data = response.json
def test_StatusCode():
    assert response.status_code==200
def test_ContentType(): 
    assert response.headers["Content-Type"]=="application/json"
def test_ContentEncoding():
    assert response.headers["Content-Encoding"]=="gzip"
def test_StatusLine():
    assert response.ok
def test_SuccessCode():
    assert data()["message"]=="Successfully! All records has been fetched."
def test_CountOfEmployees():
    assert len(data()["data"])==24