# From: https://github.com/Nitrokey/nitrokey-hotp-verification/blob/master/RFC_HOTP-test-vectors.txt
from totp import get_hotp_token


def test_get_hotp_token_gets_example_correct():
    secret = "12345678901234567890"

    expected = ['755224',
        '287082',
        '359152',
        '969429',
        '338314',
        '254676',
        '287922',
        '162583',
        '399871',
        '520489']

    actual = [get_hotp_token(secret, i) for i in range(len(expected))]

    for e, a in zip(expected, actual):
        assert e == a