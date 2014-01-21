"""
Write a program that counts the word frequencies in a plain text file.
The output should be a list of words and the number of times they appear.

Bonus items:

    1. Unicode support (try a Hebrew text file).
       Note: On Windows, you should install 'console2' for Unicode support.
"""

from word_frequencies import word_frequencies

def test_word_frequencies():
    text = "This is a plain text file. It is very very plain."
    frequencies = {
        "this": 1,
        "is": 2,
        "a": 1,
        "plain": 2,
        "text": 1,
        "file": 1,
        "it": 1,
        "very": 2,
    }

    assert word_frequencies(text) == frequencies
