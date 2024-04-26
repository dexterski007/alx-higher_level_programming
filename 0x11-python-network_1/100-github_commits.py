#!/usr/bin/python3
""" github using requests """

import requests
import sys

if __name__ == "__main__":

    owner = sys.argv[2]
    repo = sys.argv[1]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    req = requests.get(url)
    if req.status_code == 200:
        commits = req.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print("{}: {}".format(sha, author))
    else:
        pass
