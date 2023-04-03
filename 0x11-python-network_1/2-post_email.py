#!/usr/bin/python3
"""
post an email to a given url
"""
if __name__ == "__main__":
    # import request module and sys
    from urllib import request
    from urllib import parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode(email).encode("utf-8")

    # send post request and get response object
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print("Your email is: {}".format(response.read().decode("utf-8")))
