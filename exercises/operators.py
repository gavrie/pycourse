class istr(str):
    def __eq__(self, other):
        return self.lower() == other.lower()

s1 = istr("hello")
s2 = istr("Hello")
s3 = istr("hello")

def test_istr():
    assert s1 == s3
    assert s1 == s2

