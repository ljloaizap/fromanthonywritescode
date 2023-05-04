"""[Test] YT: https://youtu.be/aQH7hyJn-No
pytest's parametrize which allows you to generate many tests from one test skeleton!
Often referred to as table tests in other testing frameworks.
"""

from typing import NamedTuple
import pytest

from explains._27_pytest_parametrize import square


# region basic_parametrize_cases

def test_square_1():
    """PH"""
    assert square(1) == 1


def test_square_negative_1():
    """PH"""
    assert square(-1) == 1


def test_square_2():
    """PH"""
    assert square(2) == 4


@pytest.mark.parametrize(
    ('number', 'expected'),
    (
        (1, 1),
        pytest.param(-1, 1, id='negative_trivial_case'),
        (2, 4),
        (4, 16)
    )
)
def test_square(number, expected):
    """PH"""
    assert square(number) == expected


@pytest.mark.parametrize(
    'input_x',
    ('a', [], (), None)
)
def test_square_error(input_x):
    """PH"""
    with pytest.raises(TypeError):
        square(input_x)

# endregion


# region bad_practice

@pytest.mark.parametrize(
    ('number', 'expected', 'error'),
    (
        (1, 1, False),
        pytest.param(-1, 1, False, id='negative_trivial_case'),
        (2, 4, False),
        (4, 16, False),
        ('a', None, True),
        ([], None, True),
        ((), [], True)
    )
)
def test_square_error__not_recommended(number, expected, error):
    """PH -- Recommended NOT to do this to avoid mixing tests with that logic"""
    if error:
        with pytest.raises(TypeError):
            square(number)
    else:
        assert square(number) == expected

# ------------------------------------------------------

# endregion


# region NamedTuple_Class

class Case(NamedTuple):
    """PH"""
    input_x: int
    expected: int


@pytest.mark.parametrize(
    ('number', 'expected'),
    (
        (1, 1),
        pytest.param(-1, 1, id='negative_trivial_case'),
        Case(input_x=2, expected=4),
        (4, 16)
    )
)
def test_square_with_namedtuple(number, expected):
    """PH"""
    assert square(number) == expected

# endregion
