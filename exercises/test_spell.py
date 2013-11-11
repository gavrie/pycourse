import spell

def test_split_line():
    assert spell.split_line("hello world") == ["hello", "world"]
    assert spell.split_line("hello, world") == ["hello", "world"]

def test_strip_punctuation():
    assert spell.strip_punctuation("hello") == "hello"
    assert spell.strip_punctuation("hello,") == "hello"
    assert spell.strip_punctuation("doesn't") == "doesnt"
    assert spell.strip_punctuation("hel-lo") == "hello"
    assert spell.strip_punctuation("[hello]") == "hello"
    assert spell.strip_punctuation("(hello)") == "hello"

