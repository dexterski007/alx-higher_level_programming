#!/usr/bin/python3
""" status using requests """

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    resp = requests.get(url)
    if resp.status_code < 400:
        print(resp.text)
    else:
        print("Error code:", resp.status_code)
