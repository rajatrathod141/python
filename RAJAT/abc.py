'''
arr=[]
arr=[1,2,3,4]
ans=sum(arr)
print(ans)
a=[1,2,3]
print(sum(a))

def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[32,23,45]
n=len(arr)
ans=largest(arr,n)
print(ans)

arr=[34,56,67]
print(max(arr))
def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[1,2,3,4]
print(rlist(arr,2,len(arr)))

def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[1,2,3,4,5,6]
print(rlist(arr,3,len(arr)))

def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[11,12,13,22,33,44]
print(rlist(arr,3,len(arr)))

def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[1,2,3,4,5,6]
print(rlist(arr,3,len(arr)))

def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[44,33,22,11,9,8,7]
print(rlist(arr,3,len(arr)))

def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[1,2,3,4,5,6]
print(rlist(arr,3,len(arr)))

def rlist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[1,3,5,7]
print(rlist(arr,1,len(arr)))


def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[1,2,3,4]
print(slist(nlist))

def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[4,5,6]
print(slist(nlist))


def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[1,2,3,4]
print(slist(nlist))

def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[3,3,4]
print(slist(nlist))

def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[2,3,4,6]
print(slist(nlist))

def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[12,11,13]
print(slist(nlist))

def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[1,2,6,7]
print(slist(nlist))

def slist(nlist):
    nlist[0],nlist[-1]=nlist[-1],nlist[0]
    return nlist
nlist=[1,2,3,4]
print(slist(nlist))


def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[1,2,3,4]
pos1,pos2=1,3
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[1,2,3,4]
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[4,3,5,6]
pos1,pos1=2,3
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[11,22,33,44]
pos1,pos2=1,3
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[12,13,15,16]
pos1,pos2=2,3
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[7,8,9]
pos1,pos2=2,3
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[1,2,3,4]
pos1,pos2=1,2
print(spos(list,pos1-1,pos2-1))

def spos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[1,2,3,4]
pos1,pos2=1,4
print(spos(list,pos1-1,pos2-1))

l=[1,2,3]
print(len(l))

if(3 in l):
    print("element exist")

a=[233,44,45,5,354]
a.clear()
print(a)

b=[23,444,44,22]
b*=0
print(str(b))

a=[222,334,34]
del a[:]
print(a)

l=[1,2,3,4]
for ele in reversed(l):
    print(ele)

l=[4,5,6,7]
for i in reversed(l):
    print(i)

l=[4,3,4,2]
for i in reversed(l):
    print(i)

l=[1,2,3]
for i in l[::-1]:
    print(i)

l=[1,2,3,4]
l.reverse()
print(l)

l=[3,4,2,4]
l.reverse()
print(l)

l=[2,3,4]
l.reverse()
print(l)

l=[1,2,3]
l.reverse()
print(l)
print(sum(l))

from functools import reduce
a=[1,3,4]
b=[3,4,2]
x=reduce((lambda a,b:a*b),a)
y=reduce((lambda a,b:a*b),b)
print(x)
print(y)

from functools import reduce
a=[1,2,3]
c=reduce((lambda x,y:x*y),a)
print(c)

from functools import reduce
a=[3,4,6]
c=reduce((lambda x,y:x*y),a)
print(c)

from functools import reduce
a=[4,4,4]
c=reduce((lambda x,y:x*y),a)
print(c)

from functools import reduce
a=[2,3,2]
c=reduce((lambda x,y:x*y),a)
print(c)

from functools import reduce
a=[2,2,3]
c=reduce((lambda x,y:x*y),a)
print(c) 

l=[4,6,3,2]
l.sort()
print(l[:1])

l=[4,3,2,6]
l.sort()
print(l[:1])

l=[3,2,1]
l.sort()
print(l[:1])

l=[6,4,2]
l.sort()
print(l[:1])

l=[1,2,3]
print(min(l))

l=[3,4,2,7,8,5,4]
l.sort()
print(l[-1])

l=[33,44,55,66]
l.sort()
print(l[-1])

l=[22,33,44,1]
l.sort()
print(l[-1])

l=[3,2,4,1]
l.sort()
print(l[-1])
print(l[-2])

l=[2,3,44,34,23,23]
n=2
l.sort()
print(l[-n:])

l=[3,3,4,32,3,4,32]
n=2
l.sort()
print(l[-n:])

l=[1,2,3,4]
n=2
l.sort()
print(l[-n:])

l=[2,2,3,4]
n=2
l.sort()
print(l[-n:])

l=[12,32,123,434,5345]
for i in l:
    if(i%2==0):
        print(i,"even")
    else:
        print("odd")

l=[434,544,556,3323]
for i in l:
    if(i%2==0):
        print("even")
    else:
        print("odd")

l=[2,3,2,2,3,12,2]
for i in l:
    if(i%2==0):
        print("even")
    else:
        print
        ("odd")

l=[1,2,1,33,1,32,2]
for i in l:
    if(i%2==0):
        print(i,"even")
    else:
        print(i,"odd")

l=[2,3,21,4,2,4,2,3]
no=[no for no in l if no%2==0]
nu=[nu for nu in l if nu%2==1]
print(no)
print(nu)


l=[34,455,2,45,34]
no=[no for no in l if no%2==0]
print(no)

l=[3,3,4,43,4,3,4]
no=[no for no in l if no%2==0]
print(no)

l=[3,4,3,43,4,455,6,67]
no=[no for no in l if no%2==0]
print(no)

l=[23,4,3,45,35,5,6]
no=[no for no in l if no%2==0]
print(no)

l=[1,2,3,4,234,2]
no=[no for no in l if no%2==0]
print(no)

l=[1,2,312,3,423,3]
no=[no for no in l if no%2==0]
print(no)

l=[23,4,5,56,7,8]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[3,2,4,5,5,3]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[1,2,33,2,454,5,6]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[2,34,32,44,2]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[2,3,4,21,3,3,2]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[3,4,3,23,55,6,6,55,46,6]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[2,2,3,45,6,7,7]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[2,34,4,56,46,6]
no=list(filter(lambda x:(x%2==0),l))
print(no)

l=[3,4,2,3,44,4]
for i in l:
    if(i%2==1):
        print(i,"odd")
    else:
        print(i,"even")

l=[3,2,56,6,7,6,78,7]
for i in l:
    if(i%2==1):
        print(i,"odd")
    else:
        print(i,"even")

l=[2,3,4,5,6,7,8,8]
for i in l:
    if(i%2==1):
        print(i,"odd")
    else:
        print(i,"even")

l=[2,1,3,5,7,89,8]
for i in l:
    if(i%2==1):
        print(i,"odd")
    else:
        print(i,"even")

l=[2,3,4,2,4,3,2,4,412,4,6,78,9,8,76]
no=[no for no in l if no%2==1]
print(no)

l=[4,3,322,4,13,5,67,78,9]
no=[no for no in l if no%2==1]
print(no)

l=[23,4,556,67,7876,5777,6]
no=[no for no in l if no%2==1]
print(no)

l=[3,233,4,43443,4]
no=[no for no in l if no%2==1]
print(no)

l=[2,3,3,34,4,56,6]
no=list(filter(lambda x:(x%2==1),l))
print(no)

l=[2,3,45,65,7,8]
no=list(filter(lambda x:(x%2==1),l))
print(no)

l=[2,3,2,4,5,67,87,9,87,6,6]
no=[no for no in l if no%2==1]
print(no)

l=[2,3,32,34,45,5,6]
no=list(filter(lambda x:(x%2==1),l))
print(no)

s,e=4,9
for i in range(s,e+1):
    if(i%2==0):
        print(i,"even")

s,e=3,8
for i in range(s,e+1):
    if(i%2==0):
        print(i,"even")


s,e=2,7
for i in range(s,e+1):
    if(i%2==0):
        print(i,"even")

s,e=2,8
for i in range(s,e+1):
    if(i%2==0):
        print(i,"even")
'''










































    
