"""[Test] YT: https://youtu.be/dN-pVt7i4Us
How to test output using pytest with `capsys` and `capfd` fixtures (and why they're different)
"""

from explains._246_pytest_output import hello


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
