import requests
baseUri="https://jsonplaceholder.typicode.com"
response=requests.get(baseUri+"/todos/1")
assert response.ok