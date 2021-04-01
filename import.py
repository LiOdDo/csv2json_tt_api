import requests
import json
import os
from get_token import get_token
token = get_token("https://presales.qa.staffr.net/rest/v1/auth",
                  'presale_tt_api_test.json')

os.chdir('C:/Users/Li Li/Documents/Python/api_auto_ws/project_portal_migration/site/files')

url = "https://presales.qa.staffr.net/rest/v1/batch/file"

# Note Address line 1 can't be empty for import

with open('client_to_import.json') as json_file:
    payload = json.load(json_file)

headers = {
    'Authorization': 'Bearer '+token,
    'Content-Type': 'application/json',
    'Cookie': 'PHPSESSID=oj5olp57dls24om8cae3gi5baokbev28'
}

response = requests.request("POST", url, headers=headers, json=payload)

data = response.json()
with open('client_import_result.json', 'w') as outfile:
    json.dump(data, outfile)
