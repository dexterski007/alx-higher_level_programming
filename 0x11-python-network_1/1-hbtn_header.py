#!/usr/bin/python3
"""get header using urllib """


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.headers.get("X-Request-Id")

    print(header)
