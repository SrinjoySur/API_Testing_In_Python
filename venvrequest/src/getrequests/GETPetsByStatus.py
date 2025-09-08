import requests
baseUri="https://petstore.swagger.io/v2"
endpoint="/pet/findByStatus"
queryParam={"status":"pending"}
accept={"accept":"application/json"}
response=requests.get(baseUri+endpoint,headers=accept,params=queryParam)
# print(response.status_code)
assert response.ok
