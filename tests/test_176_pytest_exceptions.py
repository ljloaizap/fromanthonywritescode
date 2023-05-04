"""[Test] YT: https://youtu.be/6nRxZyQwwlE
How to test exceptions in pytest!
"""

import pytest

from explains._176_pytest_exceptions import parse_version, MyVersionError


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('2.7', (2, 7)),
        ('3.6', (3, 6)),
        ('3.10', (3, 10))
    )
)
def test_parse_version_success(input_s, expected):
    """PH"""
    assert parse_version(input_s) == expected


def test_parse_version_not_a_number__not_recommended():
    """There's a better way to do this"""
    try:
        parse_version('3.a')
    except ValueError as ex:
        assert ex
    else:
        raise AssertionError('expected to raise ValueError')


def test_parse_version_not_a_number__recommended():
    """PH"""
    with pytest.raises(ValueError):
        parse_version('3.a')


# def test_parse_version_not_a_number__error_on_purpose():
#     """This does not test anything. It silently passes. -- mypy packages helps here"""
#     with pytest.raises(Exception):
#         parse_version()


@pytest.mark.parametrize(
    ('version', 'expected_msg'),
    (
        ('3', "Expected #.# but got '3'"),
        ('3.6.0', "Expected #.# but got '3.6.0'"),
    )
)
def test_parse_version_failure_wrong_segment_count(version, expected_msg):
    """PH"""
    with pytest.raises(MyVersionError) as excinfo:
        parse_version(version)
    msg, = excinfo.value.args
    assert msg == expected_msg
