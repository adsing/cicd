import pytest
from mymodule import arithmetic


def test_add_pass():
    assert arithmetic.add(3, 4) == 7


def test_add_fail() -> None:
    with pytest.raises(AssertionError):
        assert arithmetic.add(3, 4) == 6


def test_subtract_pass():
    assert arithmetic.subtract(3, 4) == -1


def test_multiply_pass():
    assert arithmetic.mutliply(3, 4) == 12


def test_divide_pass():
    assert arithmetic.divide(3, 4) == 0.75


def test_divide_fail():
    with pytest.raises(ZeroDivisionError):
        assert arithmetic.divide(3, 0) == 0
