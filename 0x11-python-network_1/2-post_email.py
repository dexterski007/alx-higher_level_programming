#!/usr/bin/python3
""" status using urllib """


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]

    data = urllib.parse.urlencode({'email': mail}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        resp = response.read().decode('utf-8')

    print(resp)
