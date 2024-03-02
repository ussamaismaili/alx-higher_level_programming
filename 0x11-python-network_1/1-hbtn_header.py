#!/usr/bin/python3
""" module doc """
from urllib.request import urlopen
from sys import argv

if __name__ == '__main__':
    with urlopen(argv[1]) as response:
        print(response.headers["X-Request-Id"])
        # you can use headers attribute or info() method
