import requests
import json
import os
# add your path of your user and pwd binary file
os.chdir('C:/Users/pwd folder')


def get_token(url, access):

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
