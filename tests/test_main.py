import pytest
from your_module import closest_fibonacci

def test_closest_fibonacci():
    assert closest_fibonacci(1) == 1
    assert closest_fibonacci(2) == 2
    assert closest_fibonacci(3) == 3
    assert closest_fibonacci(4) == 3
    assert closest_fibonacci(5) == 5
    assert closest_fibonacci(6) == 5
    assert closest_fibonacci(7) == 8
    assert closest_fibonacci(8) == 8
    assert closest_fibonacci(9) == 8

def test_closest_fibonacci_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [1, 2, 3, 3, 5, 5, 8, 8, 8]
    assert [closest_fibonacci(n) for n in numbers] == expected

def test_closest_fibonacci_negative():
    with pytest.raises(ValueError):
        closest_fibonacci(-1)

def test_closest_fibonacci_non_integer():
    with pytest.raises(ValueError):
        closest_fibonacci(1.5)
