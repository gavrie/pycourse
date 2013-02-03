def log(...):
    ...

@log
def sum(a, b):
    return a + b

sum(3, 4)
sum(1, 2)


"""

Output:

>> calling sum(3, 4)
<< return 7
>> calling sum(1, 2)
<< return 3

Advanced output:

>> calling sum(3, 4) [1 time]
<< return 7
>> calling sum(1, 2) [2 times]
<< return 3

