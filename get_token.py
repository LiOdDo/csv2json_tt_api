import requests
import json
import os
# add your path of your user and pwd binary file
os.chdir('C:/Users/Li Li/Documents/postman/byoi & excels/json_jwt_authbody/')


def get_token(url, access):
    #url = "https://profservices.staffr.net/rest/v1/auth"
    #access = 'professionalservice.json'
    with open(access) as json_file:
        payload = json.load(json_file)

    headers = {
        'Content-Type': 'application/json',
        # input your PHHSESSID between = and '
        'Cookie': 'PHPSESSID=1gtjjjlkt2cm1jr4mgp2rsodqeegifg8'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    token = response.json()['auth']['token']
    print(token)
    return token
