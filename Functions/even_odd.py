def count(lst):
    even = 0 
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
        
    return even, odd

lst = [4,6,823,24,25,45,54,67,89,12,34,90,45,66,87,90]
even, odd = count(lst)
print("Even: {} and Odd : {}".format(even,odd))

