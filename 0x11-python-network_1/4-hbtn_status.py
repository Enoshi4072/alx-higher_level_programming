#!/usr/bin/python3
""" a Python script that fetches
https://alx-intranet.hbtn.io/status """
import requests
url = 'https://alx-intranet.hbtn.io/status'
try:
    response = requests.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(response.text)))
    print("\t - content: {}".format(response.text))
except Exception as e:
    print(e)
