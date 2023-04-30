""" YT: https://www.youtube.com/watch?v=K0Q5twtYxWY&ab_channel=anthonywritescode
Explanation of functools.lru_cache as well as a few ways that you might use it in your programs!

Note: in case you need to run the function again to test it it's working properly,
without the need to modify source code to remove decorator, you can call the 
underline function by accessing the __wrapped__.
"""

import functools


@functools.lru_cache
def square(number: float) -> float:
    """PH"""
    print(f'Running: {number}')
    return number * number


@functools.lru_cache(3)
def square_max_size(number: float) -> float:
    """PH"""
    print(f'Running: {number}')
    return number * number


@functools.lru_cache(maxsize=1)
def get_expensive_thing() -> int:
    """
        Let's pretend this is an expensive thing. Parameter 'maxsize' is set to 1 
        because it will ALWAYS return the same value, so there's no need to allocate 
        more resources in cache for more values (wasteful!). Some sort of 'Singleton'.
    """
    print('Running expensive code...')
    return 7
