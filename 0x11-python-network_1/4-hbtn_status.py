#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == '__main__':

    url = 'https://intranet.hbtn.io/status'

    content = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(content.text)))
    print('\t- content: {}'.format(content.text))
