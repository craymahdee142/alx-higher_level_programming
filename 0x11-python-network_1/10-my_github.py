#!/usr.bin.python3
"""A Python script that accepts your Github credentials
   (username and password) as arguments and uses Github API
   to auth request to fetch your info
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
