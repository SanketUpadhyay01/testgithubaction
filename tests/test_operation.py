from src.maths_operation import add, sub

def test_add():
    assert add(5, 3) == 8
    assert add(-1,1)== 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(-1,1)== -2
    assert sub(1,1) == 0
