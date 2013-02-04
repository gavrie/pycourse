def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def operation(op, *args):
    return op(*args)

print operation(sub, 2, 3)
