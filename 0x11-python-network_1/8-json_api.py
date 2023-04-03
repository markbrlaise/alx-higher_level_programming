#!/usr/bin/python3
"""
implementing a basic search api taking a key from the arguments that it uses to
send a post request and the response contains the JSON result
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[2] if len(argv) >= 2 else ""
    r = requests.post(url, data={'q': q})
    try:
        r_dict = r.json()
        if r_dict:
            print("[{}] {}".format(r_dict.get("id"), r_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
