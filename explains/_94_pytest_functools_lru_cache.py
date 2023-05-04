"""[Source] YT: https://youtu.be/ujRo8n0LsU4
How to test a function which is decorated with `lru_cache` with pytest!

For the sake of this exercise, I'm exchaching the executables of ruby and gem to slack and zoom,
which are some of the ones that I do have at the moment in this machine.
"""

import shutil
import functools


@functools.lru_cache(maxsize=1)
def get_default_version() -> str:
    """Returns the default language version for ruby.

    - if `slack` and `zoom` executables are both globally available: `system`
    - otherwise: `default`
    """

    if shutil.which('slack') and shutil.which('zoom'):
        return 'system'
    return 'default'
