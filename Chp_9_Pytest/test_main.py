from main import *
import pytest


def test_add():
    assert add(3, 4) == 7


def test_sub():
    assert sub(3, 4) == -1


def test_mul():
    assert mul(3, 4) == 12


def test_divide():
    with pytest.raises(ZeroDivisionError, match="Divide by Zero"):
    # assert divide(12, 0) == "Divide by Zero"
        divide(12,0)

