from array import *

arr = array('i',[])

n = int(input("Enter the array length you want to add: "))

for i in range(n):
    x = int(input("Enter the next value to add: "))
    arr.append(x)
print(arr)


val = int(input("Enter the value you want to search: "))

k=0
for e in arr: 
    if e==val:
        print("Index locatio of the number is", k)
        break
    k+=1
