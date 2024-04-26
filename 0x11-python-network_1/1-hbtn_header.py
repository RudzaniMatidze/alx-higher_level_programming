#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.rquests


if __name__ == "__main__":
    url = sys.argv[1]

    request = url.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
