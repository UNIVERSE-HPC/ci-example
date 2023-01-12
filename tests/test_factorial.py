import pytest
from mymath.factorial import factorial


def test_3():
    assert factorial(3) == 6

def test_5():
    assert factorial(5) == 120

def test_negative():
    with pytest.raises(ValueError):
      factorial(-1)
