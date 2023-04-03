#!/usr/bin/python3
"""
send a request and print the body of the response... handling HTTPError
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as er:
        print("Error code: {}".format(er.code))
