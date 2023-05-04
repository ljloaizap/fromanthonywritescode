"""[Source] YT: https://youtu.be/6nRxZyQwwlE
How to test exceptions in pytest!
"""

from typing import Tuple


class MyVersionError(ValueError):
    """Custom error to test exceptions with pytest"""


def parse_version(input_s: str) -> Tuple[int, ...]:  # Tuple[int, int]:
    """PH"""
    ret = tuple(int(part) for part in input_s.split('.'))
    if len(ret) != 2:
        raise MyVersionError(f'Expected #.# but got {input_s!r}')
    return ret
