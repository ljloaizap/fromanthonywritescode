"""YT: https://youtu.be/TJ_aGY6iyZY
Show some REAL code running in prod with unnecessary bools and learnings on how to improve it!
"""


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
