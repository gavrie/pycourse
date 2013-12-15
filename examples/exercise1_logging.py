def log(...):
    ...

@log
def mysum(a, b):
    return a + b

mysum(3, 4)
mysum(1, 2)


"""

Output:

>> calling mysum(3, 4)
<< return 7
>> calling mysum(1, 2)
<< return 3

Advanced output:

>> calling mysum(3, 4) [1 time]
<< return 7
>> calling mysum(1, 2) [2 times]
<< return 3

