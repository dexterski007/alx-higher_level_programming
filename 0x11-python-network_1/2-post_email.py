#!/usr/bin/python3
""" status using urllib """


import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

print(header)
