#!/usr/bin/python3
""" status using requests """

import requests
import sys

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    req = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': req}
    resp = requests.post(url, data=req)
    try:
        jsondata = resp.json()
        if jsondata:
            print("[{}] {}".format(jsondata.get('id'), jsondata.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
