import requests
import json
file=open("venvrequest/payloads/payload2.json","r") 
input=file.read()
payload=json.loads(input)
baseUri="https://jsonplaceholder.typicode.com"
response=requests.put(baseUri+"/posts/1",data=payload)
assert response.ok