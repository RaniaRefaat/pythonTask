class A(object):
    def foo(self):
        print ('A.foo()')

class B(object):
    def foo(self):
        print ('B.foo()')

class C(A, B):
    def foo(self):
        print ('C.foo()')
ob=C()
ob.foo() #it will call foo() from it self
#if class C dont have foo()
# it will call the first parent it goes from right to left       

        
