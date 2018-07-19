from login import make_client

client = make_client()
params={"metadataType" : "METADATA",
        "uuidProcessing" : "GENERATEUUID",
        "rejectIfInvalid": "false",
        "publishToAll": "false",
        "assignToCatalog": "false"}

URL_record = "http://localhost:8080/geonetwork/srv/api/0.1/records"

files = {'file': open('export-full-1531990103947.zip','rb')}

headers = {"Accept": "application/json, */*;" }
req = client.post(URL_record, params=params,headers=headers, files=files)

print("###### FIRST REQUEST #######")
print(req.request.headers) 
print("###### FIRST RESPONSE #######")
print(req.headers)
print("##### STATUS CODE ####")
print(req.status_code)
print("#### MESSAGE ####")
print(req.text)
