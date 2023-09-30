#!/usr/bin/python3
"""A script that:
- takes in a URL, sends a request to the URL
- and displays the value of the X-Request-Id
- variable found in the header of the response.
"""
import urllib.request
import sys
the_url = sys.argv[1]
try:
    with urllib.request.urlopen(the_url) as response:
        x_request = response.getheader('X-Request-Id')
    print(x_request)
except Exception as exp:
    print(exp)
