import requests
import json
file=open("venvrequest/payloads/payload2.json","r")
input=file.read()
payload=json.loads(input)
baseUri="https://jsonplaceholder.typicode.com"
response=requests.post(baseUri+"/posts",data=payload)
print(response.status_code)
# print(response.text)
assert response.ok