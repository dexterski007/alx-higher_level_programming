#!/usr/bin/python3
""" github using requests """

import requests
import sys

if __name__ == "__main__":

    owner = sys.argv[1]
    repo = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
