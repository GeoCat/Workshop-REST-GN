from login import make_client


client = make_client()
URL_templates = "http://localhost:8080/geonetwork/srv/api/records/templates?schema=iso19139&schema=csw-record&schema=dublin-core&schema=iso19110"
URL_data = "http://localhost:8080/geonetwork/srv/api/0.1/records/samples?schema=iso19139&schema=csw-record&schema=dublin-core&schema=iso19110"
req = client.put(URL_data, headers = {"accept": "*/*", "Content-Type": "application/json;charset=UTF-8"})
#http://localhost:8080/geonetwork/srv/api/records/samples?schema=iso19110r and response from request
print("###### FIRST REQUEST #######")
print(req.request.headers) 
print("###### FIRST RESPONSE #######")
print(req.headers)
print("##### STATUS CODE ####")
print(req.status_code)

#print(req.text)