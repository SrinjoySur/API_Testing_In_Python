import requests
baseUri="https://jsonplaceholder.typicode.com"
response=requests.delete(baseUri+"/posts/11111111")
print(response.status_code)
print(response.text)