#!/usr/bin/python3
"""
scritpt fetching https://alx-intranet.hbtn.io/status using the urllib package
"""
if __name__ == "__main__":
    # import request module from urllib package
    import urllib.request

    # establish https connection and get repsonse object as fetch
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as fet:
        # read response
        content = fet.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
