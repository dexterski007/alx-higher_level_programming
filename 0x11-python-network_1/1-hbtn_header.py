#!/usr/bin/python3
"""get header using urllib """


import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        header = response.headers.get("X-Request-Id")

    print(header)
