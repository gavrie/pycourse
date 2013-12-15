class A(object):
    def foo(self):
        print "A::foo"

class B(A):
    def foo(self):
        print "B::foo"
        super(B, self).foo()

class C(A):
    def foo(self):
        print "C::foo"
        super(C, self).foo()

class D(B, C):
    def foo(self):
        print "D::foo"
        super(D, self).foo()


obj = D()
obj.foo()
