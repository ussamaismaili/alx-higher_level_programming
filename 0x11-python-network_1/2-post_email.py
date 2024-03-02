#!/usr/bin/python3
"""module doc"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    data = {'email': argv[2]}
    encoded_data = urlencode(data).encode('utf-8')
    # create request object
    request = Request(url, encoded_data, method='POST')

    with urlopen(request) as response:
        result = response.read()
        print(result.decode('utf-8'))
