#!/usr/bin/env python
#Using requests since it is the simplest library
#http://docs.python-requests.org/en/master/
# HTTP 403
import sys
import requests


def make_client(URL="http://localhost:8080/geonetwork/srv/eng/catalog.signin", user = "admin", password ="admin"):
    """Makes login and returns request object """


    login_url = URL
    login_user = user
    login_password = password

    client = requests.session() #session will create a cookie system
    client.post(URL) #POST so that we obtain the XSRF-TOKEN 

    client.headers.update({"X-XSRF-TOKEN": client.cookies["XSRF-TOKEN"]})
    req = client.post(login_url ,auth=(login_user, login_password))
    if req.status_code == 200:
        return client
    else: 
        return None
    
