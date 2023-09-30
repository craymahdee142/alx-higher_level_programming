#!/usr/bin/python3
"""
Python script that takes in url
 -- send request to the url
 -- displays the body o the response - decoded in utf-8
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
