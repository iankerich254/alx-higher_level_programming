#!/usr/bin/python3
"""
Takes in URL, sends a request to URL, and displays value of the X-Request-Id
"""
import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers.get('X-Request-Id'))
