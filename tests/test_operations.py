from src.math_operations import add, sub, mult

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0


def test_sub():
    assert sub(5,3) == 2
    assert sub(1,1) == 0
    assert sub(2,3) == -1

def test_mult():
    assert mult(5,3) == 15
    assert mult(1,1) == 1
    assert mult(2,3) == 6
