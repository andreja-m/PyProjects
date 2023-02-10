#!/usr/bin/env python3

import urllib.parse
import urllib.request

url = 'https://gnu.org'
with urllib.request.urlopen(url) as response: # GET
    content = response.read()

print(content)
