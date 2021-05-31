'''
class A:
    def m1(self):
        print("m1....A")


class B:
    def m2(self):
        print("m2....B")

class C(A,B):
    def m3(self):
        pass
    def __mro__(self):
        pass
c=C()
c.m1()
c.m2()
c.m3()
print(c.mro())

class A:
    def m1(self):
        print("AAAA")

class B(A):
    def m2(self):
        print("BBBB")

class C(A):
    def m3(self):
        print("CCCC")
    def m1(self):
        print("M1...C")
class D(B,C):
    pass
d=D()
d.m1()
d.m2()
d.m3()
d.m1()
o=A()
o.m1()

class A:
    def m1(self):
        print("A")
class B(A):
    def m2(self):
        print("B")

class C(A):
    def m3(self):
        print("C")
    def m2(self):
        print("M2C")
class D(B,C):
    pass

c=C()
c.m3()
c.m2()
c.m1()
o=B()
o.m2()

class A:
    def m1(self):
        print("A")
class B(A):
    def m2(self):
        print("B")
class C(A):
    def m3(self):
        print("C")
    def m3(self):
        print("M3C")
class D(B,C):
    pass
c=C()
c.m3()
c.m3()
c.m1()
o=B()
o.m2()
n=C()
n.m3()


class A:
    def m1(self):
        print("A")
class B(A):
    def m2(self):
        print("B")
class C(A):
    def m3(self):
        print("C")
    def m1(self):
        print("M1C")
class D(B,C):
    pass
c=C()
c.m3()
c.m1()
o=B()
o.m1()
o.m2()


def add(a,b):
    c=a+b
    print(c)
add(3,1)

def add(a,b,d):
    c=a+b
    print(c)
add(4,2)

def add(a,b):
    c=a+b
    print(c)
add(4,3)

def add(a,b,d=0):
    c=a+b
    print(c)
add(4,3)

def add(a,b):
    c=a+b
    print(c)
add(3,5)

def add(a,b,d=0):
    c=a+b
    print(c)
add(3,5)

def add(a,b):
    c=a+b
    print(c)
add(3,6)
def add(a,b,d=0):
    c=a+b
    print(c)
add(6,4)

class Parent:
    def m1(self):
        print("M1...P")
class Child(Parent):
    def m1(self):
        print("M1..Child")
c=Child()
c.m1()
p=Parent()
p.m1()           


class P:
    def m1(self):
        print("P")
class C(P):
    def m1(self):
        print("C")
c=C()
c.m1()
c.m1()
p=P()
p.m1()
'''
class P:
    def m1(self):
        print("P")
class C(P):
    def m1(self):
        print("C")
c=C()
c.m1()

class P:
    def m1(self):
        print("P")
class C(P):
    def m1(self):
        print("C")
c=C()
c.m1()
p=P()
p.m1()















































        





















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
