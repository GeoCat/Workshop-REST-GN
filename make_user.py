from login import make_client

client = make_client()
URL_users = "http://localhost:8080/geonetwork/srv/api/0.1/users"
pay_load = {
  "addresses": [
    {
      "address": "",
      "city": "Wageningen",
      "country": "string",
      "id": 2,
      "state": "Gelderland",
      "zip": "6707JJ"
    }
  ],
  "email": [
    "jorge.dejesus@geocat.net"
  ],
  "emailAddresses": [
    "jorge.dejesus@geocat.net"
  ],
  "enabled": "True",
  "groupsEditor": [
    "Administrator"
  ],
  "groupsRegisteredUser": [
    "Administrator"
  ],
  "groupsReviewer": [
    "Administrator"
  ],
  "groupsUserAdmin": [
    "Administrator"
  ],
  "id": 2,
  "kind": "Administrator",
  "name": "Jorge Samuel Mendes de Jesus",
  "organisation": "Geocat B.V",
  "password": "sheep",
  "profile": "Administrator",
  "surname": "",
  "username": "shaun"
}
req = client.put(URL_users, headers = {"accept": "application/json"}, json = pay_load)
print(req.text)
