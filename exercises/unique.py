"""
1. Write a function that determines if a string has all unique characters.
2. What if you can not use additional data structures?
"""

def unique(s):
   d = set()
   for letter in s:
       if letter in d:
           return False
       d.add(letter)
   return True


def test_unique():
    assert unique("house")
    assert not unique("direction")
