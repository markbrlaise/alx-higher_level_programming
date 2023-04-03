#!/usr/bin/python3
"""
scritpt fetching https://alx-intranet.hbtn.io/status using the requests package
"""
import requests

if __name__ == "__main__":
    # send a get request and get response object
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
