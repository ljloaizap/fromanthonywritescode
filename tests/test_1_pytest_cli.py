"""[Test] YT: https://youtu.be/sv46294LoP8
Building out a simple skeleton for a command line interface in python
and showing how to test it with pytest!
"""

import pytest
from explains import _1_pytest_cli


def test_main(capsys):  # Capsys: capture system output
    """PH"""
    _1_pytest_cli.main(['Lili'])

    out, err = capsys.readouterr()
    assert out == 'Welcome to the jungle Lili!\n'
    assert err == ''


def test_main_error_with_empty_string(capsys):
    """PH"""
    _1_pytest_cli.main([''])

    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Person's name must not be empty!\n"


def test_main_error_with_empty_string_raises_system_exit(capsys):
    """PH"""
    with pytest.raises(SystemExit) as excinfo:
        _1_pytest_cli.print_with_args_default_raise_system_exit([''])

    retv, = excinfo.value.args
    assert retv == 1

    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Person's name must not be empty!\n"
