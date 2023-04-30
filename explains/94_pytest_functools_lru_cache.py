"""YT: https://www.youtube.com/watch?v=ujRo8n0LsU4&ab_channel=anthonywritescode
How to test a function which is decorated with `lru_cache` with pytest!

For the sake of this exercise, I'm exchaching the executables of ruby and gem to slack and zoom,
which are some of the ones that I do have at the moment in this machine.
"""

import shutil
import functools

import pytest

from unittest import mock


@functools.lru_cache(maxsize=1)
def get_default_version() -> str:
    """Returns the default language version for ruby.

    - if `slack` and `zoom` executables are both globally available: `system`
    - otherwise: `default`
    """

    if shutil.which('slack') and shutil.which('zoom'):
        return 'system'
    return 'default'


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
