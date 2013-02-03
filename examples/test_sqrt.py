import pytest
from sqrt0 import square

def test_square():
    assert square(0) == 0
    assert square(1) == 1
    assert square(-1) == 1

def test_square_string_fails():
    with pytest.raises(TypeError):
        assert square("hello") == "?"
