'''
num=int(input("enter number"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag =True
            break
if flag:
    print("not prime")
else:
    print(" prime")

num=int(input("enter number"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print("not prime")
else:
    print("prime")

num=int(input("enter number"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag = True
            break
if flag:
    print("not prime")
else:
    print("prime")

num=int(input("enter number"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print("not prime")
else:
    print("prime")

num=int(input("enter number"))
flag=False
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag=True
            break
if flag:
    print("not prime")
else:
    print("prime")

num=int(input("enter number"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print("not prime")
else:
    print("prime")


x,y=0,1
while y<15:
    print(y)
    x,y=y,x+y

x,y=0,1
while y<10:
    print(y)
    x,y=y,x+y

x,y=0,1
while y<10:
    print(y)
    x,y=y,x+y

x,y=0,1
while y<10:
    print(y)
    x,y=y,x+y


def fib(n):
    a=0
    b=1
    if n<0:
        print("incorrect")
    elif n==0:
        return 0
    elif n==1:
        return b
    else:
        print(a,b,end='')
        for i in range(2,n):
            c=a+b
            print(c,end='')
            a=b
            b=c
        return b
print(fib(7))




a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
    

a=int(input("enter terms"))
f=0
s=1
if a<=0:
    print("the requested series is",f)
else:
    print(f,s,end="")
    for x in range(2,a):
        next=f+s
        print(next,end="")
        f=s
        s=next

a=int(input("enter terms"))
f=0
s=1
if a<=0:
    print(f)
else:
    print(f,s,end='')
    for x in range(2,a):
        next=f+s
        print(next,end='')
        f=s
        s=next

a=int(input("enter terms"))
f=0
s=1
if a<=0:
    print(f,end="")
else:
    print(f,s,end="")
    for x in range(2,a):
        next=f+s
        print(next,end="")
        f=s
        s=next

a=int(input("enter terms"))
f=0
s=1
if a<=0:
    print(f)
else:
    print(f,s,end='')
    for x in range(2,a):
        next=f+s
        print(next,end='')
        f=s
        s=next


string=input("enter string")
if (string==string[::-1]):
    print("palindrome")
else:
    print("not")

n=input("enter string:")
if(n==n[::-1]):
    print("palindrome")
else:
    print("not")

n=input("enter string")
if(n==n[::-1]):
    print("palindrome")
else:
    print("not")

n=input("enter string")
if(n==n[::-1]):
    print("palindrome")
else:
    print("not")


num=int(input("enter value:"))
temp=num
rev=0
while (num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("palindrome")
else:
    print("not")

num=int(input("enter number"))
temp=num
rev=0
while (num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("palindrome")
else:
    print("not")

num=int(input("enter number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("palindrome")
else:
    print("not")


num=int(input("enter number"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("palindrome")
else:
    print("not")

'''

num=int(input("enter number"))
temp=num
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig**3
    num=num//10
if(temp==sum):
    print("armstrong")
else:
    print("not")

num=int(input("enter numbr"))
temp=num
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig**3
    num=num//10
if(temp==sum):
    print("armstrong")
else:
    print("not")

num=int(input("enter number"))
temp=num
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig**3
    num=num//10
if(temp==sum):
    print("armstrong")
else:
    print("not")

num=int(input("enter number"))
temp=num
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig**3
    num=num//10
if(temp==sum):
    print("armstrong")
else:
    print("not")










    












        






















    






































            
