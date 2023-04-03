#!/usr/bin/python3
"""
using the GitHub API to display my id with HTTPBasicAuth
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth)
    print((r.json().get("id")))
