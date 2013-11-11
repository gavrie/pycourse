#!/usr/bin/env python
import sys
import re

def main():
    words = set()

    words_file = open("words")
    for line in words_file:
        word = line.strip()
        words.add(word)
    words_file.close()

    for line in sys.stdin:
        pass

def split_line(line):
    parts = line.strip().split()
    return [strip_punctuation(p) for p in parts]

def strip_punctuation(word):
    return re.sub("[.\"!;?\-,'\[\]()]", "", word)

if __name__ == '__main__':
    main()
