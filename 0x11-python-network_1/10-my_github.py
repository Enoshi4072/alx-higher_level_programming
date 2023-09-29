#!/usr/bin/python3
""" script takes your GitHub credentials
(username and password) and uses
the GitHub API to display your id """
import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    token = sys.argv[2]

    session = requests.Session()
    session.auth = (username, token)
    url = 'https://api.github.com/user'
    try:
        response = session.get(url)
        user_d = response.json()
        user_info = user_d.get('id', 'None')
        print(user_info)
    except Exception as e:
        print("None")
else:
    print("Provide details")
