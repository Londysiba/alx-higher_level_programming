#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- response: {}'.format(response))
    print('\t- utf8 response: {}'.format(str(response)[2:-1]))
