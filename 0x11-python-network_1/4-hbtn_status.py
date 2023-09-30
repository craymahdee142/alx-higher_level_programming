#!/usr/bin/python3
"""Pyhton script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    res = request.get('https://alx-intranet.hbtn.io/status')
    print("Body response")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
