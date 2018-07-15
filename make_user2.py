from login import make_client

client = make_client()

URL_users = "http://localhost:8080/geonetwork/srv/api/0.1/user/actions/register"
pay_load = {
  "address": {
    "address": "string",
    "city": "string",
    "country": "string",
    "id": 2,
    "state": "string",
    "zip": "string"
  },
  "captcha": "string",
  "email": "jorge.dejesus@geocat.net",
  "name": "string",
  "organisation": "string",
  "profile": "Administrator",
  "surname": "string",
  "username": "jorge"
}
req = client.put(URL_users, headers = {"accept": "application/json"}, json = pay_load)
print(req.text)
