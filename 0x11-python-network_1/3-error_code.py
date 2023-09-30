#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8). """
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code:"e.code)
