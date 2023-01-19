# def fact(x):
#     x = int(input("Enter the value of x: "))
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     print(f)

# fact(5)

# Recurssion: A function calling itself is called recurssion.




def fact(n):
    if (n==0):
        return 1
    f = n * fact(n-1)
    return f
    
result = fact(5)
print(result)
