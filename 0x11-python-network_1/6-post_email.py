#!/usr/bin/python3
""" module doc """
import requests
from sys import argv

if __name__ == "__main__":
    parameters = {'email': argv[2]}
    response = requests.post(url=argv[1], data=parameters)
    print(response.text)
