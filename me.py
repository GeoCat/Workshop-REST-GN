from login import make_client

client = make_client()
URL_me = "http://localhost:8080/geonetwork/srv/api/0.1/me"
if client:
    print("Using token: {}".format(client.cookies["XSRF-TOKEN"]))


req = client.get(URL_me, headers = {"accept": "application/json"})
print(""" STATUS """)
print(req.status_code)
print(""" RESPONSE """)
print(req.json())