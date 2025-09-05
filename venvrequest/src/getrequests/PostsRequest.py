import requests
baseUri="https://jsonplaceholder.typicode.com"
response=requests.get(baseUri+"/todos/1111/comments")
print(response.status_code)
print(response.text)