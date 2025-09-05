import requests
baseUri="https://jsonplaceholder.typicode.com"
response=requests.delete(baseUri+"/posts/1")
assert response.ok