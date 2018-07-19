from login import make_client
import glob
client = make_client()

params={"metadataType" : "METADATA",
        "uuidProcessing" : "GENERATEUUID",
        "rejectIfInvalid": "false",
        "publishToAll": "false",
        "assignToCatalog": "false"}

URL_record = "http://localhost:8080/geonetwork/srv/api/0.1/records"

headers = {"Accept": "application/json, */*;" }
for zip in glob.glob("./data/*zip"):
    files = {'file': open(zip,'rb')}
    
    req = client.post(URL_record, params=params,headers=headers, files=files)
    print(req.status_code)
