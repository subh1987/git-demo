# def fibo(n):
#     a = 0
#     b = 1 
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b 
#         b = c
#         print(c)
# fibo(10)


# If input is 1 then also 2 o/p coming in above, so extra if condition to get right o/p 
def fibo(n):
    a = 0
    b = 1 

    if n == 1:
        print(a)

    else: 
        print(a)
        print(b)
    for i in range(2,n):
        c = a + b
        a = b 
        b = c
        print(c)
fibo(1)
