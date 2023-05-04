"""[Source] YT: https://youtu.be/aQH7hyJn-No
pytest's parametrize which allows you to generate many tests from one test skeleton!
Often referred to as table tests in other testing frameworks.
"""


def square(number: int) -> int:
    """Note: this should be in another place separated from tests. """
    return number * number
