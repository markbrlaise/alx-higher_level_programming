#!/usr/bin/python3
"""
send a request and display value of a header
"""
if __name__ == "__main__":
    # import request module
    import sys
    from urllib import request

    # get response object after the request sent using urlopen function
    with request.urlopen(sys.argv[1]) as response:
        # get headers from response object and display the value required
        print(dict(response.headers).get("X-Request-Id"))
