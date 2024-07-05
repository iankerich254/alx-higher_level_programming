#!/usr/bin/python3
"""
Takes in a URL, sends request to URL, & displays body of response.
Manages urllib.error.HTTPError exceptions and prints: Error code: status code.
"""
import sys
import urllib.error
import urllib.request

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
