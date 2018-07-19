#using owslib
#http://localhost:8080/geonetwork/srv/en/csw?request=GetCapabilities&service=CSW&version=2.0.2

URL= "http://localhost:8080/geonetwork/srv/en/csw"

from owslib.csw import CatalogueServiceWeb
from owslib.fes import PropertyIsEqualTo

csw = CatalogueServiceWeb(URL)


birds_query = PropertyIsEqualTo('csw:AnyText', 'KNMI')
csw.getrecords2(constraints=[birds_query], maxrecords=20)

for rec in csw.records:
    print(csw.records[rec].title)
    print((csw.records[rec].identifier))
    

import requests
URL_record = "http://localhost:8080/geonetwork/srv/api/0.1/records/{}".format(csw.records[rec].identifier)
req = requests.get(URL_record,  headers = {"Accept": "application/xml"})
print(req.text)