#!/usr/bin/python3
import sys
import requests

response = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))

if response.status_code == 200:
    print(response.json().get("id"))
else:
    print("None")