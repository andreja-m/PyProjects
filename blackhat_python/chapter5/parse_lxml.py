#!/usr/bin/env python3

from io import BytesIO
from lxml import etree

import requests

url = 'https://gnu.org'
r = requests.get(url)   # GET
content = r.content     # contetn is of type 'bytes'

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser) # Parse into tree

for link in content.findall('//a'): # find all "a" anchor
    print(f"{link.get('href')} -> {link.text}")
