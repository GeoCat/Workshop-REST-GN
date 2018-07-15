from login import make_client

client = make_client()
#curl -X GET "https://vanilla.geocat.net/geonetwork/srv/api/0.1/users" -H  "accept: application/json" -H  "X-XSRF-TOKEN: a713e74d-e68a-44e8-ad34-91abc02be72a"
URL_users = "http://localhost:8080/geonetwork/srv/api/0.1/users"
req = client.get(URL_users, headers = {"accept": "application/json"})
print(req.text)
