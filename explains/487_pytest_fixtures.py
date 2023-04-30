"""YT: https://www.youtube.com/watch?v=ScEQRKwUePI&ab_channel=anthonywritescode
Go over all the options and use cases for fixtures in pytest!
"""
import tempfile
import pytest
from util import flag


class MyClass:
    """PH"""

    def function_f(self):
        """PH"""
        return 1

    def function_g(self):
        """PH"""
        return 2


# region if you had this... there's a better way to do it

def test_function_f__before():
    """PH"""
    flag('Started TC: test_function_f__before')
    my_class = MyClass()  # meh. Let's use fixtures -> my_class_fixture
    assert my_class.function_f() == 1


def test_function_g__before():
    """PH"""
    flag('Started TC: test_function_g__before')
    my_class = MyClass()  # meh. Let's use fixtures -> my_class_fixture
    assert my_class.function_g() == 2

# endregion


# region fixture: 2 different types (Return & Yield)

# Type 1: Return fixtures
@pytest.fixture
def my_class_fixture():
    """PH"""
    return MyClass()


# Type 2: Yield fixtures
@pytest.fixture
def temporary_dir():
    """PH"""
    with tempfile.TemporaryDirectory() as tmpdir:
        flag('In fixture temporary_dir: before yield')
        yield tmpdir
    flag('In fixture temporary_dir: after yield')


# Here I am combining fixtures with other fixtures to use it as a parameter
@pytest.fixture
def my_class_fixture_with_another_fixture(temporary_dir):
    """PH"""
    flag('In fixture my_class_fixture_with_another_fixture')
    return MyClass()


@pytest.fixture
def setup_teardown():
    """PH"""
    flag('In fixture setup_teardown: setup')
    yield
    flag('In fixture setup_teardown: teardown')


def test_with_my_class_fixture_with_another_fixture(my_class_fixture_with_another_fixture):
    """This is to test a fixture inside another fixture as param"""
    flag('Started TC: test_with_my_class_fixture_with_another_fixture')


def test_with_setup_teardown(setup_teardown):
    """PH"""
    flag('Started TC: test_with_setup_teardown')


def test_function_f__new(my_class_fixture, temporary_dir):
    """PH"""
    flag('Started TC: test_function_f__new')
    assert my_class_fixture.function_f() == 1
    flag(temporary_dir)


def test_function_g__new(my_class_fixture, temporary_dir):
    """PH"""
    flag('Started TC: test_function_g__new')
    assert my_class_fixture.function_g() == 2
    flag(temporary_dir)


# endregion


# region Trigger fixtures

# 1) How to trigger fixtures with mark.usefixtures
@pytest.mark.usefixtures('setup_teardown')
def test_trigger_fixture_with_usefixtures(my_class_fixture, temporary_dir):
    """PH"""
    flag('Started TC: test_trigger_fixture_with_usefixtures')
    assert my_class_fixture.function_g() == 2
    flag(
        f'In test_trigger_fixture_with_usefixtures, temporary dir = {temporary_dir}')


# 2) How to trigger fixtures with autouse param. With or without scope.
# @pytest.fixture(autouse=True, scope='session')
@pytest.fixture(autouse=True)
def setup_teardown_with_autouse():
    """PH"""
    flag('In fixture setup_teardown_with_autouse --> setup')
    yield
    flag('In fixture setup_teardown_with_autouse --> teardown')


def test_simple_case():
    """PH"""
    flag('Started TC: test_simple_case')
    assert MyClass().function_f() == 1

# endregion


# region Renaming fixture

@pytest.fixture(name='fix')
def dlkasdlkjald_ugly_function_name():
    """PH"""
    return 5


def test_with_set_and_teardown_renaming_fixture(fix):
    """PH"""
    flag(f'In test_with_set_and_teardown_renaming_fixture: {fix=}')

# endregion


# region Using params in a fixture (sort of parametrize)

@pytest.fixture(params=(1, 2, 3, 4))
def an_int(request):
    """PH"""
    yield request.param + 2


def test_an_int(an_int):
    """PH"""
    flag('Started TC: test_an_int')
    flag(f'Got {an_int=}')

# endregion


# region sharing fixtures

class TestMyThing:
    """PH"""

    @pytest.fixture
    def fix(self):
        """PH"""
        yield 10

    def test_1(self, fix):
        """PH"""
        flag(f'In TestMyThing.test_1 ---------- Got {fix=}')

# endregion
