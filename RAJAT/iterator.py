val='abc'
obj=iter(val)
while True:
    try:
        item=next(obj)
        print(item)
    except StopIteration:
        break
val=[1,2,3,4]
obj=iter(val)
while True:
    try:
        item=next(obj)
        print(item)
    except StopIteration:
        break
    

val='pqr'
obj=iter(val)
while True:
    try:
        item=next(obj)
        print(item)
    except StopIteration:
        break

val='abcd'
obj=iter(val)
while True:
    try:
        item=next(obj)
        print(item)
    except StopIteration:
        break


















