"""Unnecessary bools"""


def morning(number: int | None) -> bool:
    """Function"""
    # if number == 1:
    #     return True
    # else:
    #     return False

    # return True if number else False
    # return number
    return bool(number)


print(morning(1))
