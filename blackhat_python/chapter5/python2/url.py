#!/usr/bin/env python2

# This is Python2 script

import urllib2

url = 'https://www.gnu.org'

response = urllib2.urlopen(url) # GET

print(response.read())
response.close()
