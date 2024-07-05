#!/usr/bin/python3
"""
Takes in a URL & an email, sends a POST req.,& displays body of the response.
"""
import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
email = {'email': sys.argv[2]}
data = urllib.parse.urlencode(email).encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    print(response.read().decode('utf-8'))
