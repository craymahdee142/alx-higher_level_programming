#!/usr/bin/python3
"""
Python script that takes in url
 --and displays it value of the X-Request-id
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print('response.headers.get("X-Request-Id"))
