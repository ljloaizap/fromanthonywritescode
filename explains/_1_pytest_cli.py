"""[Source] YT: https://youtu.be/sv46294LoP8
Building out a simple skeleton for a command line interface in python
and showing how to test it with pytest!
"""

import argparse
import sys
from typing import Optional
from typing import Sequence


def print_with_parser():
    """This parser takes arguments running program in script mode"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'person', help='Person name to be displayed in the cli')
    args = parser.parse_args()

    print(f'Welcome to the jungle {args.person}!')


def print_with_args_default(argv: Optional[Sequence[str]] = None) -> int:
    """This parser takes arguments in direct call as well as params 
    with argv while importing current module"""
    parser = argparse.ArgumentParser()
    parser.add_argument('person', help='Person name that will be shown in CLI')
    args = parser.parse_args(argv)

    if args.person == '':
        print("Person's name must not be empty!", file=sys.stderr)
        return 1

    print(f'Welcome to the jungle {args.person}!')
    return 0


def print_with_args_default_raise_system_exit(argv: Optional[Sequence[str]] = None) -> int:
    """ It raises an Exception call SystemExit. 
        This function was created only to be tested with pytest """
    sys.exit(print_with_args_default(argv))


def main(argv: Optional[Sequence[str]] = None) -> int:
    """PH"""
    # print_with_parser()  # python <module_name> <person>
    return print_with_args_default(argv)  # import module and use default argv


if __name__ == "__main__":
    sys.exit(main())
