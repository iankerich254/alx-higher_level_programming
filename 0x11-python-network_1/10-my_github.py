#!/usr/bin/python3
"""
Takes GitHub credentials (username and password)
and uses the GitHub API to display the user ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

username = sys.argv[1]
password = sys.argv[2]
url = 'https://api.github.com/user'

response = requests.get(url, auth=HTTPBasicAuth(username, password))
print(response.json().get('id'))
