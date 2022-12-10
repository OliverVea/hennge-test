"""Used to send the POST request to Company"""

import hashlib
import argparse
import requests
from requests.auth import HTTPBasicAuth

from totp import get_totp_token

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url', type=str)
parser.add_argument('-U', '--username', type=str)
parser.add_argument('-s', '--secret', type=str)

args = parser.parse_args()


def main():
    """The main method of the solution."""
    secret = args.username + args.secret
    password = get_totp_token(secret=secret, digits=10, digest=hashlib.sha512)
    auth = HTTPBasicAuth(args.username, password)

    headers = {
        "Content-Type": "application/json"
    }

    with open('solution.json', 'r', encoding='utf-8') as file:
        data = file.read()

    response = requests.post(args.url, data=data, headers=headers, auth=auth, timeout=30)
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    main()
