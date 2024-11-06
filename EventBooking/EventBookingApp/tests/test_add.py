from add import add
import pytest

def test_add():
    assert add(3,5)==8
    assert add(4,4)==8

# def neg_add():
#     assert add(-3,-5)==8