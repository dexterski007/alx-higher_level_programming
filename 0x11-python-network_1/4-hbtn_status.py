#!/usr/bin/python3
""" status using requests """

import requests

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)

    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)
