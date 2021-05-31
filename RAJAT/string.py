'''
s=input("enter string")
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=''.join(l1)[::-1]
print(output)

string = "I am a python programmer"

words = string.split()

words = list(reversed(words))

print(" ".join(words))


s=input("enter string:")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)

s=input("enter string:")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)

s=input("enter string")
print(s[::-1])
print(''.join(reversed(s)))

s=input("enter string")
print(s[::-1])
print(''.join(reversed(s)))


s=input("enter string")
print(s[::-1])
print(''.join(reversed(s)))

s=input("enter string")
print(s[::-1])
print(''.join(reversed(s)))

s=input("enter string")
print(s[::-1])
print(''.join(reversed(s)))


s=input("enter string")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)

s=input("enter string")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)

s=input("enter string")
i=len(s)-1
t=''
while i>=0:
    t=t+s[i]
    i=i-1
print(t)

s=input("enter string")
i=len(s)-1
t=''
while i>=0:
    t=t+s[i]
    i=i-1
print(t)


s=input("enter string")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=''.join(l1)
print(output)

s=input("enter string")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=''.join(l1)
print(output)

s=input("enter string")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=''.join(l1)
print(output)
s=input("enter string")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=''.join(l1)
print(output)

s=input("enter string")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=''.join(l1)
print(output)

s=input("enter string")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=''.join(l1)
print(output)

s="i am the best"
for i in s[::]:
    print(i,end='')
for i in s[::-1]:
    print(i,end='')

s="wow it is"
for i in s[::]:
    print(i,end='')
for i in s[::-1]:
    print(i,end='')


s="welcome girl"
for i in s[::]:
    print(i,end='')

for i in s[::-1]:
    print(i,end='')

s="how are you"
for i in s[::]:
    print(i,end='')
for i in s[::-1]:
    print(i,end='')


s=input("enter string")
subs=input("enter subs")
if subs in s:
    print(subs,"found")
else:
    print(subs,"not found")

s=input("enter string")
subs=input("enter subs")
if subs in s:
    print(subs,"found")
else:
    print(subs,"not found")

s=input("enter string")
subs=input("enter subs")
if subs in s:
    print(subs,"found")
else:
    print(subs,"not found")

s=input("enter string")
subs=input("enter subs")
if subs in s:
    print(subs,"found")
else:
    print(subs,"not found")


s1=input("enter frst strng")
s2=input("enter scnd strng")
if s1==s2:
    pprint("equal")
elif s1>s2:
    print("frst grtr")
else:
    print("frst lssr")

s1=input("ennter frst strng")
s2=input("enter scnd strrng")
if s1==s2:
    print("equal")
elif s1<s2:
    print("frst less")
else:
    print("frst grtr")

s1=input("enter frst strng")
s2=input("enter scnd strng")
if s1==s2:
    print("equal")
elif s1>s2:
    print("frst grtr")
else:
    print("frst less")
         
s1=input("enter frst strng")
s2=input("enter scnd strng")
if s1==s2:
    print("equal")
elif s1<s2:
    print("frst less")
else:
    print("frst grtr")


city=input("enter city")
scity=city.strip()
if scity=='pune':
    print("hello pune")
elif scity=='pusad':
    print("hi pusad")
else:
    print("invalid")

s='abcaaa'
print(s.count('a'))
print(s.count('b'))

s="hello hi"
s1=s.replace("hi","dear")
print(s1)

s="wow its"
s1=s.replace("its","good")
print(s1)
s="hey how"
s1=s.replace("how","babe")
print(s1)
s="hey ha"
s1=s.replace("ha","wow")
print(s1)

s="welcome to here"
l=s.split()
for i in l:
    print(i)

s="how you"
l=s.split()
for i in l:
    print(i)


s="it is a"
l=s.split()
for i in l:
    print(i)

s="good to go"
l=s.split()
for i in l:
    print(i)
t=('abc','pqrpr')
s='-'.join(t)
print(s)

t=('a','s','d')
s='*'.join(t)
print(s)

t=('q','w','e')
s='-'.join(t)
print(s)
t=('f','f','g')
s='-'.join(t)
print(s)

t=('r','u','o')
s='-'.join(t)
print(s)

name="abc"
salary=40000
print("{}'s salary is{}".format(name,salary))
print("{0}'s salary is {1}".format(name,salary))

name="asd"
sal=34234
print("{}'s sal is {}".format(name,sal))
print("{0}'s sal is {1}".format(name,sal))   

name="zxc"
sal=1234
print("{}'s sal is {}".format(name,sal))
print("{0}'s sal is{1}".format(name,sal))

name="dfg"
sal=33344
print("{}'s sal is {}".format(name,sal))
print("{0}'s sal is {1}".format(name,sal))


s=input("enter string")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

s=input("enter string")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

s=input("enter string")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

s=input("enter string")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)
'''

s=input("enter string")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)
    

s=input("enter string")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)

s=input("enter ssstring")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)

s=input("enter string")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)

s=input("enter string")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)

s=input("enter string")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)















        
























            



















    











































    
    














    












































