from login import make_client
client = make_client()
#curl -X GET "https://vanilla.geocat.net/geonetwork/srv/api/0.1/csw/virtuals" -H  "accept: application/json" -H  "X-XSRF-TOKEN: null"
#https://vanilla.geocat.net/geonetwork/doc/api/
#http://localhost:8080/geonetwork/srv/en/csw?request=GetCapabilities&service=CSW&version=2.0.2
URL_users = "https://vanilla.geocat.net/geonetwork/srv/api/0.1/csw/virtuals"
req = client.get(URL_users,headers = {"accept": "application/json"})
print(req.text)