import requests
queryParams={"q":"hyderabad","appid":"a503b144b4273f8bfc4636c01a447bc3"}
url="http://api.openweathermap.org/data/2.5/weather"
response=requests.get(url,params=queryParams)
responseBody=response.json()
def test_statusCode():
    assert response.ok
def test_city():
    assert responseBody["name"]=="Hyderabad"
def test_country():
    assert responseBody["sys"]["country"]=="IN"
def test_minTemp():
    assert responseBody["main"]["temp_min"]>0
def test_Temp():
    assert responseBody["main"]["temp"]>0