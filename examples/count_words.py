from fizzbuzz import text

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.setdefault(word, 0) + 1

for word, count in word_count.items():
    if count > 1:
        print word, count
