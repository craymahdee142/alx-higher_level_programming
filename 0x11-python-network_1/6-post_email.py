#!/usr/bin/python
"""
Python script that takes in url
 -- sends a POST request to the passed, takes email as parameter
 -- displays the body o the response
"""


import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    # create HTTP POST request
    request = urllib.request.Request(url)
    # send request and capture the response
    with urllib.request.urlopen(request) as reponse:
        print(dict(response.headers).get("X-Required-ID"))
