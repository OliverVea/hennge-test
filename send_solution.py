import hashlib
import requests
from requests.auth import HTTPBasicAuth
from totp import get_totp_token

URL = "https://echo.zuplo.io/" # "https://api.challenge.hennge.com/challenges/003"
USERNAME = "oliver.vea@gmail.com"
SECRET = USERNAME + "HENNGECHALLENGE003"
DIGITS = 10
HASHING_METHOD = hashlib.sha512


def main():
    password = get_totp_token(secret=SECRET, digits=DIGITS, digest=HASHING_METHOD)
    auth = HTTPBasicAuth(USERNAME, password)

    headers = {
        "Content-Type": "application/json"
    }

    with open('solution.json', 'r', encoding='utf-8') as f:
        data = f.read()

    response = requests.post(URL, data=data, headers=headers, auth=auth, timeout=30)
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    main()
