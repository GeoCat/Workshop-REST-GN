from login import make_client

client = make_client()
URL_users = "http://localhost:8080/geonetwork/srv/api/records/templates?schema=iso19139"
#http://localhost:8080/geonetwork/srv/api/records/templates?schema=iso19139&schema=csw-record&schema=dublin-core&schema=iso19110
req = client.put(URL_users, headers = {"accept": "*/*"})
print(req.text)