'''
def sum(items):
    sum_n=0
    for x in items:
        sum_n+=x
    return sum_n
print(sum([1,2,3]))

n=[1,2,3]
print(sum(n))

def mul(items):
    t=1
    for x in items:
        t*=x
    return t
print(mul([4,6]))

def mul(items):
    t=1
    for x in items:
        t*=x
    return t
print(mul([2,3]))

def mul(items):
    t=1
    for x in items:
        t*=x
    return t
print(mul([6,7]))


def mul(items):
    t=1
    for x in items:
        t*=x
    return t
print(mul([4,8]))

d={3:6,2:1,4:3}
print(sorted(d.items(),reverse=True))

d={1:2,3:4}
d.update({6:7})
print(d)

d1={1:1}
d2={2:2}
d3={3:3}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

d1={12:12}
d2={13:13}
d3={34:34}
d4={}
for d in(d1,d2,d3):
    d4.update(d)
print(d4)

d1={1:1}
d2={2:2}
d3={3:3}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

d1={1:1}
d2={2:2}
d3={3:3}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)



d={4:6,7:8,1:1,2:2}
x=4
if x in d:
    print("key present")
else:
    print("no")
    
d={1:1}
x=1
if x in d:
    print("present")
else:
    print("no")

d={'a':7,'b':8}
for key,value in d.items():
    print(key,value)

n = int(input("enter number"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
    print(d)

n=int(input("enter number"))
dict={}
for x in range(1,n+1):
    d[x]=x*x
    print(d)

n=int(input("enter number"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
    print(d)

n=int(input("enter number"))
d=dict={}
for x in range(1,n+1):
    d[x]=x*x


d=dict()
for x in range(1,4):
    d[x]=x*x
    print(d)
d=dict()
for x in range(1,4):
    d[x]=x*x
    print(d)
d=dict()
for x in range(1,4):
    d[x]=x*x
    print(d)

d=dict()
for x in range(1,4):
    d[x]=x*x
    print(d)    
            
    print(d)

d1={1:1}
d2={2:2}
d1.update(d2)
print(d1)
d1={3:3}
d2={4:4}
d1.update(d2)
print(d1)
d1={6:6}
d2={7:7}
d1.update(d2)
print(d1)
d1={8:8}
d2={9:9}
d1.update(d2)
print(d1)


d={1:1,2:2,3:3}
for key,value in d.items():
    print(key,value)
    
d={1:1,2:2,3:3}
print(sum(d.values()))


d={'a':3,'b':6}
r=1
for value in d:
    r=r*d[value]
    print(r)
d={6:7,8:4}
result=1
for key in d:
    result=result*d[key]
    print(result)
d={4:6,7:8}
result=1
for value in d:
    result=result*d[value]
    print(result)

d={1:2,3:4}
del d[3]
print(d)

k=[1,2,3]
v=[4,5,6]
d=dict(zip(k,v))
print(d)

k=[7,2,3]
v=[4,5,6]
d=dict(zip(k,v))
print(d)

k=[8,9,7]
v=[3,4,2]
d=dict(zip(k,v))
print(d)

k=[44,33,22]
v=[77,88,99]
d=dict(zip(k,v))
print(d)


d={4:3,7:9,6:2}
print(sorted(d))
d={8:23,6:56,2:345}
print(sorted(d))

d={7:5,4:7,6:6}
print(sorted(d))

d={6:4,3:4,7:6}
print(sorted(d))


d={44:34,43:54}
print(max(d))
print(min(d))
print(sum(d))

d={23:45,46:67}
print(min(d))
print(max(d))
print(sum(d))

d={3:4,6:6}
print(min(d))
print(max(d))
print(sum(d))

d={7:3,6:7}
print(min(d))
print(max(d))
print(sum(d))



d={1:1,2:2,3:3,2:2,3:3}
result={}
or key,value in d.items():
    if value not in result.values():
        result[key]=value
        print(result)

d={2:3,4:6,2:3}
result={}
for key,value in d.items():
    if value not in result.values():
        result[key]=value
        print(result)



d={3:3,4:4,4:5,6:7}
result={}
for key,value in d.items():
    if value not in result.values():
        result[key]=value
        print(result)

d={1:1,2:2,3:3,2:2}
result={}
for key,value in d.items():
    if value not in result.values():
        result[key]=value
        print(result)


d={}
if not bool (d):
    print("empty")
else:
    print("not")
    

d={}
if not bool(d):
    print("empty")
else:
    print("not empty")

d={}
if not bool(d):
    print("empty")
else:
    print("not")


d={}
if not bool(d):
    print("empty")
else:
    print("not")

    
from collections import Counter
d1={2:4}
d2={3:2}
d=Counter(d1)+Counter(d2)
print(d)

from collections import Counter
d1={2:3,4:6}
d2={7:8,6:1}
d=Counter(d1)+Counter(d2)
print(d)

from collections import Counter
d1={1:1}
d2={2:2}
d=Counter(d1)+Counter(d2)
print(d)

from collections import Counter
d1={4:4}
d2={6:6}
d=Counter(d1)+Counter(d2)
print(d)

from heapq import nlargest
d={1:1,2:3,4:6,7:8}
print(nlargest(2,d,key=d.get))

from heapq import nlargest
d={0.12:0.13,0.23:0.12,0.43:0.44}
print(nlargest(2,d,key=d.get))

from heapq import nlargest
d={45:34,46:23,24:345}
print(nlargest(2,d,key=d.get))

from heapq import nlargest
d={3:4,2:5,1:6}
print(nlargest(2,d,key=d.get))  


l=[1,2,34,4]
d=c={}
for n in l:
    c[n]={}
    c=c[n]
    print(d)

l=[1]
d=c={}
for n in l:
    c[n]={}
    c=c[n]
    print(d)

l=[1,2]
d=c={}
for n in l:
    c[n]={}
    c=c[n]
    print(d)

l=[3,4]
d=c={}
for n in l:
    c[n]={}
    c=c[n]
    print(d)

from heapq import nlargest
from operator import itemgetter
d={1:2,32:4,52:63,71:8,45:56,67:79}
for name,value in nlargest(2,d.items(),key=itemgetter(1)):
    print(name,value)

from heapq import nlargest
from operator import itemgetter
d={3:4,2:3,6:7}
for name,value in nlargest(2,d.items(),key=itemgetter(1)):
    print(name,value)


from heapq import nlargest
from operator import itemgetter
d={3:4,5:6,7:8}
for name,value in nlargest(2,d.items(),key=itemgetter(1)):
    print(name,value)

from heapq import nlargest
from operator import itemgetter
d={6:7,4:6,3:4}
for name,value in nlargest(2,d.items(),key=itemgetter(1)):
    print(name,value)

n={3:2,7:6,8:3}
print(list(n)[0])
print(list(n)[1])
print(list(n)[2])

n={7:8,4:6,6:4}
print(list(n)[0])
print(list(n)[1])
print(list(n)[2])

n={6:4,2:3,1:4}
print(list(n)[0])
print(list(n)[1])
print(list(n)[2])

n={8:9,4:5,2:3}
print(list(n)[0])
print(list(n)[1])
print(list(n)[2])



d={1:1,2:3}
r=list(map(list,d.items()))
print(r)

d={1:2}
r=list(map(list,d.items()))
print(r)

d={2:4}
r=list(map(list,d.items()))
print(r)

d={6:7}
r=list(map(list,d.items()))
print(r)



def test(dict):
    result={key:[id for id in val if not id%2]for key,val in d.items()}
    return result
d={'a':[2,4],'c':[1,2]}
print(test(d))
'''    

from collections import Counter
def test(dict):
    result=Counter(d.items())
    return result
d={'a':2,'b':2,'a':1}
print(test(d))

from collections import Counter
def test(dict):
    result=Counter(d.items())
    return result
d={1:1,1:2,1:3}
print(test(d))

from collections import Counter
def test(dict):
    result=Counter(d.items())
    return result
d={'q':'a','b':'c'}
print(test(d))

from collections import Counter
def test(dict):
    result=Counter(d.items())
    return result
d={1:1,2:2,1:1,2:2}
print(test(d))





























































    

