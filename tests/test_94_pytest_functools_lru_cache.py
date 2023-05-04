"""[Test] YT: https://youtu.be/ujRo8n0LsU4
How to test a function which is decorated with `lru_cache` with pytest!
"""

import shutil

from unittest import mock
import pytest

from explains._94_pytest_functools_lru_cache import get_default_version


# region not recommended

# @pytest.fixture(autouse=True)
@pytest.fixture
def clear_lru_cache():
    """PH"""
    get_default_version.cache_clear()
    yield
    get_default_version.cache_clear()


@pytest.mark.usefixtures('clear_lru_cache')
def test_both_slack_and_zoom_exist__not_recommended():
    """PH"""
    with mock.patch.object(shutil, 'which', return_value='/some/exe'):
        assert get_default_version() == 'system'


@pytest.mark.usefixtures('clear_lru_cache')
def test_neither_slack_nor_zoom_exist__not_recommended():
    """PH"""
    with mock.patch.object(shutil, 'which', return_value=None):
        assert get_default_version() == 'default'

# endregion


# region recommended

def test_both_slack_and_zoom_exist__recommended():
    """PH"""
    with mock.patch.object(shutil, 'which', return_value='/some/exe'):
        assert get_default_version.__wrapped__() == 'system'


def test_neither_slack_nor_zoom_exist__recommended():
    """PH"""
    with mock.patch.object(shutil, 'which', return_value=None):
        assert get_default_version.__wrapped__() == 'default'

# endregion
