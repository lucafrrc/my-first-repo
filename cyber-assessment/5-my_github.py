#!/usr/bin/python3
import sys
import requests

url = "https://api.github.com/user"
response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

try:
    print(response.json().get("id"))
except ValueError:
    print("None")