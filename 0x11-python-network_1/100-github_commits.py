#!/usr/bin/python3
"""
interview practice at holberton
listing 10 most recent commits to a repo
"""
import sys
from requests import get, auth

if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = get(url)
    commits = r.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
