#!/usr/bin/python3
""" status using requests """

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    mail = sys.argv[2]
    data = {'email': mail}

    resp = requests.post(url, data)

    print(resp.text)
