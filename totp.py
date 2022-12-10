"""Used to generate HOTP and TOTP passwords."""

import base64, hashlib, time
import pyotp


def encode_secret(secret: str) -> bytes:
    """Encodes the secret for generating a OTP.

    Encoding is ascii followed by base32 encoding.

    Args:
        secret: The secret to encode.

    Returns:
        The encoded bytes.
    """
    secret_encoded = secret.encode('ascii')
    secret_base32 = base64.b32encode(secret_encoded)
    return secret_base32


def get_hotp_token(secret: str, count: int, digest = hashlib.sha1, digits: int = 6) -> str:
    """Gets a HOTP (HMAC One Time Password) token.

    Args:
        secret: The secret used to generate the token.
        count: The current password count to generate.
        digest: The hash function used to generate the token.
        digits: The number of digits to return.

    Returns:
        A valid HOTP based on the provided arguments.
    """
    secret_base32 = encode_secret(secret)
    hotp = pyotp.HOTP(secret_base32, digest=digest, digits=digits)
    return hotp.at(count)


def get_totp_token(secret: str, digest = hashlib.sha1, digits: int = 6, time_step: int = 30) -> str:
    """Gets a TOTP (Time-based One Time Password) token, based on the time the method is called.

    Args:
        secret: The secret used to generate the token.
        digest: The hash function used to generate the token.
        digits: The number of digits to return.

    Returns:
        A valid TOTP based on the provided arguments.
    """
    count = int(time.time()) // time_step
    token = get_hotp_token(secret, count, digest, digits)

    if len(token) < digits:
        token = token.ljust(6, '0')

    return token


def main():
    """The main function used to test the module."""
    secret = "12345678901234567890"
    token = get_hotp_token(secret, 0)
    expected = "755224"
    assert expected == token


if __name__ == '__main__':
    main()
