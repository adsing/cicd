# import sys
# sys.path.append("/home/user/Desktop/github/temp/src")

from mymodule import arithmetic as arithmetic


def test_add_correct():
    assert arithmetic.add(3, 4) == 7
