'''
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return-1

arr=[2,3,32,34,42,14345,242,42]
print(sorted(arr),end="")

def isort(arr):
    for i in range(1,len(arr)):
        a=arr[i]
        j=i-1
        while j>=0 and a<arr[j]:
            #j-i=1
            arr[j+1]=a
arr=[23,23,454,3211,12,1,321,2]
isort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def isort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            #j-i=1
            arr[j+1]=key
arr=[6,4,32,1,2,4,2]
isort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def isort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=key
arr=[3,2,1]
isort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

a=[34,243,1,3,4,2]
print(sorted(a))
'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[3,4,5,1,2]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[6,4,5,3,45,5,4]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[75678,97,0,865,5435,7]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[6,4,25,7,78,468,65,54]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[4,46,78,32,56,7,67,7]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[54,3,56,3,57,65,85]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[4,5,3,6,3,6,8,9,3]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

def bsort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[2,3,45,2,42,4]
bsort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])























            






































