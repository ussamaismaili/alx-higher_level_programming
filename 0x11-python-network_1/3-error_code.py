#!/usr/bin/python3
"""module doc"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    try:
        with urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    except HTTPError as e:
        print('Error code:', e.code)
