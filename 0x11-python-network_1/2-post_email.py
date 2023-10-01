#!/usr/bin/python
"""
Python script that takes in url
 -- sends a POST request to the passed, takes email as parameter
 -- displays the body o the response
"""


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.request.parse.urlencode(value).encode("ascii")

    # create HTTP POST request
    request = urllib.request.Request(url, data)
    # send request and capture the response
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
