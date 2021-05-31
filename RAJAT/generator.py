'''
def sampl():
    yield 1
    yield 2
    yield 3
for value in sampl():
    print(value)

def m1():
    yield 1
    yield 2
for i in m1():
    print(i)

def sampl():
    yield 1
    yield 2
for i in sampl():
    print(i)

def smpl():
    yield 6
    yield 7
for i in smpl():
    print(i)

def smpl():
    yield 44
    yield 34
x=smpl()
print(x.__next__())
print(x.__next__())


def smpl():
    yield 54
    yield 34
x=smpl()
print(x.__next__())
print(x.__next__())

def smpl():
    yield 67
    yield 56
x=smpl()
print(x.__next__())
print(x.__next__())

l=[1,2,3]
for i in l:
    print(i)
a=iter(l)
print(a.__next__())
print(a.__next__())
print(a.__next__())

l=[6,7,8]
for i in l:
    print(i)
a=iter(l)
print(a.__next__())
print(a.__next__())
print(a.__next__())

l=[3,6,7]
for i in l:
    print(i)
a=iter(l)
print(a.__next__())
print(a.__next__())
print(a.__next__())

l=['a','b','c']
for i in l:
    print(i)

a=iter(l)
print(a.__next__())
print(a.__next__())
print(a.__next__())
'''

def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
x=fib(4)
print(x.__next__())
print(x.__next__())
print(x.__next__())

def fib(num):
    a,b=0,1
    while a<num:
        yield a
        a,b=b,a+b
x=fib(3)
print(x.__next__())
print(x.__next__())
print(x.__next__())

def fib(num):
    a,b=0,1
    while a<num:
        yield a
        a,b=b,a+b
x=fib(3)
print(x.__next__())
print(x.__next__())
print(x.__next__())

def fib(num):
    a,b=0,1
    while a<num:
        yield a
        a,b=b,a+b
x=fib(3)
print(x.__next__())
print(x.__next__())
print(x.__next__())























        


















    























    
