#!/usr/bin/python3
"""
Python script that takes in url
 -- send request to the url
 -- displays the body o the response - decoded in utf-8
"""


if __name__ == "__main__":
    import sys
    rom urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
