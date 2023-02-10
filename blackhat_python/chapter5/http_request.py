#!/usr/bin/env python3

import requests

url = 'https://boodelyboo.com'
response = requests.get(url) # GET

data = {'user': 'tim', 'passwd': '31337'}
response = request.post(url, data=data) # POST
print(response.text) # response.text = string;
response.content = bytestring
