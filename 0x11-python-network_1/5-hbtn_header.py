#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        x_request = requests.get(url)
        print(x_request.headers['X-Request-Id'])
    except Exception as e:
        print(e)
