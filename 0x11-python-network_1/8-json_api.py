#!/usr/bin/python3
""" module doc """
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ''
    parameters = {'q': q}
    response = requests.post(url, data=parameters)
    try:
        json_response = response.json()
        if len(json_response) == 0:
            print('No result')
        else:
            id, name = json_response['id'], json_response['name']
            print(f'[{id}] {name}')
    except Exception:
        print('Not a valid JSON')
