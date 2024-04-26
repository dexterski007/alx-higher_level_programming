#!/usr/bin/python3
""" status using urllib """


import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
mail = sys.argv[2]

data

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

print(header)
