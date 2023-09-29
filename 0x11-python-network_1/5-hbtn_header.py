#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the value of the variable
X-Request-Id in the response header """
import requests
import sys
url = sys.argv[1]
try:
    x_request = requests.get(url)
    if 'X-Request-Id' in x_request.headers:
        x_req = x_request.headers['X-Request-Id']
        print(x_req)
except Exception as e:
    print(e)
