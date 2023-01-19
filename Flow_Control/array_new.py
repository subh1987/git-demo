
# from array import *
# vals = array('i',[5,7,9,10])

# print(vals)
# print(type(vals))

from array import *

arr = array('i',[])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the the next value"))
    arr.append(x)

print(arr)

val = int(input("Enter the value you want to search: "))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
