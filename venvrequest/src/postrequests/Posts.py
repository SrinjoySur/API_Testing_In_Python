import requests
import json
file=open("venvrequest\payloads\payload2.json","r") # type: ignore
input=file.read()
payload=json.loads(input)
baseUri="https://jsonplaceholder.typicode.com"
response=requests.post(baseUri+"/posts/1",data=payload)
print(response.status_code)
print(response.text)