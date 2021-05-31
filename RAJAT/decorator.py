'''
def decorator(func):
    def wrapper(*args,**kwargs):
        print('*'*4)
        func(*args,**kwargs)
        print('*'*2)
    return wrapper
def hi():
    print("hello")

@decorator
def by():
    print("byeee")

hi=decorator(hi)
hi()
by()

def decorator(func):
    def inner(*args,**kwargs):
        print("start")
        func(*args,**kwargs)
        print("end")
    return inner

def m1():
    print("method")

@decorator
def n1():
    print("nnnn")

m1=decorator(m1)
m1()
n1()

def decorator(func):
    def wrapper(*args,**kwargs):
        print("start")
        func(*args,**kwargs)
        print("end")
    return wrapper
def m1():
    print("m1")
@decorator
def m2():
    print("m2")
m1=decorator(m1)
m1()
m2()

def decorator(func):
    def wrapper(*args,**kwargs):
        print("start")
        func(*args,**kwargs)
        print("end")
    return wrapper
def m1():
    print("m1")
@decorator
def m2():
    print("m2")

m1=decorator(m1)
m1()
m2()



def E_handler(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except TypeError:
            print(f"{func.__name__}: wrong data type")
    return inner
@E_handler
def mean(a,b):
    print((a+b)/2)
@E_handler
def square(sq):
    print(sq*sq)
@E_handler
def divide(a,b):
    print(a/b)
mean(2,4)
square(4)
divide(6,4)
mean("two")

def e_handler(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except TypeError:
            print(f"{func.__name__} wrong data type")
    return inner

@e_handler
def mean(a,b):
    print((a+b)/2)
@e_handler
def square(sq):
    print(sq*sq)
@e_handler
def divide(a,b):
    print(a/b)

mean(3,4)
square(4)
divide(4,4)
mean("one")

def e_handler(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except TypeError:
            print(f"{func.__name__} wrong data type")
    return inner
@e_handler
def mean(a,b):
    print((a+b)/2)
@e_handler
def square(sq):
    print(sq*sq)
@e_handler
def divide(a,b):
    print(a/b)

mean(2,4)
square(4)
divide(4,4)


def e_handler(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except TypeError:
            print(f"{func.__name__} wrong data type")
    return inner
@e_handler
def mean(a,b):
    print((a+b)/2)
@e_handler
def square(sq):
    print(sq*sq)
@e_handler
def divide(a,b):
    print(a/b)
mean(3,4)
square(3)
divide(4,4)



class A:
    def decorator(func):
        def inner(self):
            print("start")
            func(self)
            print("end")
        return inner
    @decorator
    def fun1(self):
        print("class A")

class B:
    @decorator
    def fun2(self):
        print("class B")

obj=B()
obj.fun1()
obj.fun2()



class check_no:
    def decor(func):
        def check(no):
            func(no)
            if no%2==0:
                print("even")
            else:
                print("odd")
        return check
    @decor
    def is_even(no):
        print("user input:",no)

obj=check_no
obj.is_even(44)
        
class check_no:
    def decor(func):
        def check(no):
            func(no)
            if no%2==0:
                print("even")
            else:
                print("odd")
        return check
    @decor
    def is_even(no):
        print(no)
obj=check_no
obj.is_even(3)

class check_no:
    def decor(func):
        def check(no):
            func(no)
            if no%2==0:
                print("even")
            else:
                print("odd")
        return check
    @decor
    def is_even(no):
        print(no)
obj=check_no
obj.is_even(6)

class check_no:
    def decor(func):
        def check(no):
            func(no)
            if no%2==0:
                print("even")
            else:
                print("odd")
        return check
    @decor
    def is_even(no):
        print(no)
obj=check_no
obj.is_even(4)

'''








                








































    

















    

          






































        
