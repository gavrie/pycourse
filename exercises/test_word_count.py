"""
Write a program that counts the count of characters, words and lines
in its input, similar to the Unix "wc" command.

Example output when run on the contents of this file:

    $ python word_count.py test_word_count.py
    29 lines
    86 words
    635 characters

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
