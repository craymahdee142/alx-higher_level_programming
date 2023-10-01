#!/usr/bin/python3
"""
Python script that takes in url
 -- sends a request to url and displays it value
 -- of the X-Request-id variable of header
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
