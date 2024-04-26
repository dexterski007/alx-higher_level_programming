#!/usr/bin/python3
""" status using requests """

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
