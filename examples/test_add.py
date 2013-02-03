from add import add

def test_add_with_wrong_result():
    assert add(3, 4) == 5

def test_add_with_correct_result():
    assert add(3, 4) == 7

