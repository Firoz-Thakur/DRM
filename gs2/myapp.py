import requests
import json
URL=""


data={'name':'sonam',
       'roll':101,
       'city':'ranchi',
}

json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)