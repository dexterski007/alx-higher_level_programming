#!/usr/bin/python3
""" github using requests """

import requests
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    usern = sys.argv[1]
    passw = sys.argv[2]

    req = requests.get(url, auth=(usern, passw))
    if req.status_code == 200:
        userdata = req.json()
        print(userdata['id'])
    else:
        print(None)
