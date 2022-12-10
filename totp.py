import base64, hashlib, time
import pyotp


def encode_secret(secret: str):
    secret_encoded = secret.encode('ascii')
    secret_base32 = base64.b32encode(secret_encoded)
    return secret_base32


def get_hotp_token(secret: str, count: int, digest=hashlib.sha1, digits: int = 6) -> str:
    secret_base32 = encode_secret(secret)
    hotp = pyotp.HOTP(secret_base32, digest=digest, digits=digits)
    return hotp.at(count)


def get_totp_token(secret: str, digest, digits: int, time_step: int = 30):
    count = int(time.time()) // time_step
    token = str(get_hotp_token(secret, count, digest, digits))

    if len(token) < 6:
        token = token.ljust(6, '0')

    return token


def main():
    secret = "12345678901234567890"
    token = get_hotp_token(secret, 0)
    expected = "755224"
    assert expected == token


if __name__ == '__main__':
    main()
