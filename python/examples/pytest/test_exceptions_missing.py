import pytest

def divide(a, b):
    return None if b == 0 else a / b

def test_zero_division():
    with pytest.raises(ValueError) as e:
        divide(1, 0)
    assert str(e.value) == 'Cannot divide by Zero' 

