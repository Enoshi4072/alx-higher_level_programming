#!/usr/bin/python3
"""  takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8) """
import urllib.request
import sys
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')
try:
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("{}".format(body))
except Exception as e:
    print(e)