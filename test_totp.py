"""Tests for TOTP and HOTP generation"""

from totp import get_hotp_token


def test_get_hotp_token_gets_example_correct():
    """Verifies that the output passwords are correct, based on the source:
    https://github.com/Nitrokey/nitrokey-hotp-verification/blob/master/RFC_HOTP-test-vectors.txt"""
    secret = "12345678901234567890"

    expecteds = ['755224',
        '287082',
        '359152',
        '969429',
        '338314',
        '254676',
        '287922',
        '162583',
        '399871',
        '520489']

    actuals = [get_hotp_token(secret, i) for i in range(len(expecteds))]

    for expected, actual in zip(expecteds, actuals):
        assert expected == actual
