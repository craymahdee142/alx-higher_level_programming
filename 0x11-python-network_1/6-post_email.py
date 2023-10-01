#!/usr/bin/python3
"""
Python script that takes in url
 -- sends a POST request to the passed, takes email as parameter
 -- displays the body o the response
"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    res = requests.post(url, data=value)
    print(res.text)
