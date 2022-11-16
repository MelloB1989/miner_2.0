import requests
import json

url = "http://3.16.44.57/id.json"
set_json = requests.get(url)
instance_details = json.loads(set_json.text)

ip = instance_details["Reservations"][0]["Instances"][0]["PublicIpAddress"]
state = instance_details["Reservations"][0]["Instances"][0]["State"]["Name"]
print(ip+state)