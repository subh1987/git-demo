## Anonymious function, without decalring function. Lamda function
# f = lambda a,b : a+b

# result = f(5,6)

# print(result)

from functools import reduce

nums = [3,2,4,8,4,5,7,6,10,9]

evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*2,evens))
print(evens)
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)
print(sum)