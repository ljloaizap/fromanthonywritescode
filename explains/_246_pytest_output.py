"""YT: https://youtu.be/dN-pVt7i4Us
How to test output using pytest with `capsys` and `capfd` fixtures (and why they're different)
"""
import subprocess
import sys

# region source_code


def hello(name: str) -> None:
    """PH"""
    print(f'hello hello {name}')


def hello_subprocess(name: str) -> None:
    """PH"""
    subprocess.check_call(('echo', 'hello', 'hello', name))


def main():
    """PH"""
    # hello(sys.argv[1])
    hello_subprocess(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())

# endregion

# region tests


def test_hello_capsys(capsys):
    """PH"""
    hello('lili')
    stdout, _ = capsys.readouterr()
    assert stdout == 'hello hello lili\n'


# def test_hello_capsys_subprocess(capsys):
#     """This test fails because capsys doesn't capture what subprocess prints in console"""
#     hello_subprocess('lolo')
#     stdout, stderr = capsys.readouterr()
#     assert stdout == 'hello hello lolo\n'

def test_hello_capfd(capfd):
    """PH"""
    hello('michi')
    stdout, _ = capfd.readouterr()
    assert stdout == 'hello hello michi\n'


# endregion
