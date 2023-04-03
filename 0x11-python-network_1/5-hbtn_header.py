#!/usr/bin/python3
"""
send a request and get vlaue of X-Request-Id in response header
"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
