#!/usr/bin/python3
"""
Takes in URL, sends req to URL, & displays body of response.
If HTTP status code is >= 400, prints: Error code: HTTP status code.
"""
import sys
import requests

url = sys.argv[1]
response = requests.get(url)
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
