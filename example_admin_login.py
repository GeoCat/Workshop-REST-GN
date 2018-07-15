#!/usr/bin/env python
#Using requests since it is the simplest library
#http://docs.python-requests.org/en/master/
# HTTP 403
import sys
import requests


login_url = 'http://localhost:8080/geonetwork/srv/eng/catalog.signin'
login_url = 'http://localhost:8080/geonetwork/srv/eng/catalog.signin'
login_user = "admin"
login_password = "admin"

client = requests.session() #session will create a cookie system
req = client.post(login_url) #POST so that we obtain the XSRF-TOKEN 

#Header and response from request
print("###### FIRST REQUEST #######")
print(req.request.headers) 
print("###### FIRST RESPONSE #######")
print(req.headers)
print("##### STATUS CODE ####")
print(req.status_code)


client.headers.update({"X-XSRF-TOKEN": client.cookies["XSRF-TOKEN"]})
req = client.post(login_url ,auth=(login_password, login_password))

print("###### SECOND REQUEST #######")
print(req.request.headers) 
print("###### SECOND RESPONSE #######")
print(req.headers)
print("##### STATUS CODE ####")
print(req.status_code)