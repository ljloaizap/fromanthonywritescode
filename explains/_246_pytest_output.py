"""[Source] YT: https://youtu.be/dN-pVt7i4Us
How to test output using pytest with `capsys` and `capfd` fixtures (and why they're different)
"""

import subprocess
import sys


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
