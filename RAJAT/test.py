'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)


l=[3,2,344,24,3]
s=set(l)
print(s)
t=tuple(l)
print(t)

s={2,34,5,76}
l=list(s)
print(l)

t=(1,1,1,2,2,2,4,5,6)
l=list(t)
print(l)
s=set(t)
print(s)

# isabs function
import os
out = os.path.isabs("/baz/foo")
print(out)

def isort(a): 
    for x in range(1, len(a)): 
        k = a[x]  #element present at index number 1
        j = x-1
        while j >=0 and k < a[j] :      #comparing elements with the next until the last item 
                a[j+1] = a[j] 
                j -= 1         #comparing each element to the elements present to its left 
        a[j+1] = k     #new item becomes the key
 
a = [24, 56, 1, 50, 17] 
isort(a) 
print(a)

class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")
  
# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")
  
r = C()
  
# it prints the lookup order 
print(C.__mro__)
print(C.mro())
'''
a = float(input("Enter A:"))

b = float(input("Enter B:"))

c = a * a + b * b
print(c)





















