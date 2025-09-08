import requests
import json
file=open("venvrequest/payloads/PetStorePayload.json")
input=file.read()
payload=json.loads(input)
baseUri="https://petstore.swagger.io/v2/pet"
# requestEndpoint="/pet"
contentType={"Content-Type":"application/json","accept":"application/json"}
reponse=requests.post(baseUri,data=payload,headers=contentType)
responseBody=reponse.json
print(reponse.status_code)
print(reponse.text)
assert reponse.ok
assert isinstance(responseBody,dict)
assert "id" in responseBody
# file.close()