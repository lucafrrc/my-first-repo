#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]  # aqui será o token passado como argumento
    
    response = requests.get("https://api.github.com/user", auth=(username, password))
    
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
