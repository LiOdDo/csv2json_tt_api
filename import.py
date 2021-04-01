import requests
import json
import os
from get_token import get_token
token = get_token("baseURL/auth",
                  'userpwd.json')

os.chdir('C:/Users/data source folder')

url = "baseURL/batch/file"

# Note Address line 1 can't be empty for import

with open('client_to_import.json') as json_file:
    payload = json.load(json_file)

headers = {
    'Authorization': 'Bearer '+token,
    'Content-Type': 'application/json',
    'Cookie': 'PHPSESSID=insertyourSESSIDhere'
}

response = requests.request("POST", url, headers=headers, json=payload)

data = response.json()
with open('client_import_result.json', 'w') as outfile:
    json.dump(data, outfile)
