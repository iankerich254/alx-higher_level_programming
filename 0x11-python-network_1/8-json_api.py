#!/usr/bin/python3
"""
Takes in letter & sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

url = 'http://0.0.0.0:5000/search_user'
q = sys.argv[1] if len(sys.argv) > 1 else ""
data = {'q': q}

response = requests.post(url, data=data)
try:
    json_response = response.json()
    if json_response:
        print(f"[{json_response.get('id')}] {json_response.get('name')}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
