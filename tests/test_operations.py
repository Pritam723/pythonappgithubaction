from src.math_operations import add, sub, multiply

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0


def test_sub():
    assert sub(5,3) == 2
    assert sub(1,1) == 0
    assert sub(2,3) == -1

def test_mult():
    assert multiply(5,3) == 15
    assert multiply(1,1) == 1
    assert multiply(2,3) == 6
