#!/usr/bin/python3
""" takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter. """
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    q_data = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        response = requests.post(url, data=q_data)
        try:
            json_d = response.json()
            if json_d:
                print("[{}] {}".format(json_d['id'], json_d['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except Exception as e:
        print("No result")
