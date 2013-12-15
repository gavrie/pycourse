def foo(a, b, *args):
    print a, b, args

# foo(1, 2, 4)

def bar(a=None, b=None, c=None, d=None, e=None, f=None):
    print a,b,c,d,e,f

# keyword args

bar(a=1,
    c=3,
    f=7,
    d=8)
