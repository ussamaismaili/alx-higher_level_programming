#!/usr/bin/python3
""" module doc """
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
    print(f"Body response:\n\t- type: {type(body)}\n\t\
- content: {body}\n\t- utf8 content: {body.decode('utf8')}")
