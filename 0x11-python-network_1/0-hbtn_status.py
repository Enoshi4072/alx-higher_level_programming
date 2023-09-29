#!/usr/bin/python3
"""  Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request
the_url = 'https://alx-intranet.hbtn.io/status'
try:
    with urllib.request.urlopen(the_url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
except Exception as exp:
    print(exp)
