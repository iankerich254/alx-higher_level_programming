#!/usr/bin/python3
"""
Takes in URL & email, sends POST req to passed URL with email as parameter,
and finally displays the body of the response.
"""
import sys
import requests

url = sys.argv[1]
email = {'email': sys.argv[2]}
response = requests.post(url, data=email)
print(response.text)
