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
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
