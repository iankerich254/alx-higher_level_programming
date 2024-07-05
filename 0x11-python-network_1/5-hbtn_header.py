#!/usr/bin/python3
"""
Takes in URL, sends req to URL, & displays value of the variable X-Request-Id.
"""
import sys
import requests

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))
