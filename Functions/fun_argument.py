# def add(name,age):   # x,y are format arguments 
#     # c = x + y
#     # print(c)
#     print(name)
#     print(age)


# add("subhankar",35)   # actual argument 
# add(age=36,name='subhankar') # age= and name= are the keyword while passing values
# # it is required while we are not passing the values in proper position

# def add(name,age=18): #if we declare the values then no need to pass duing called fucntion.
#     print(name)
#     print(age)
# add('subhankar Das') # not passing the age as it's predefined and mandatory age=18

# variable length function, define a fun where no of arguments are not fixed

# def sum(a, *b):
#    c = a

#     for i in b:
#         c = c + i 
#     print("value of C is ", c)

# sum(4,5,6,7)
# sum(1,2,3,4,5,6,7,8,9)

# def sum(*b):
#     c = 0 
#     for i in b:
#         c = c + i 

#     print(c)
# sum(5,8,9,2,3,4,5)
 
     
# where parameter passed but multiple like age= , city= ** means 2 data
def person(name,**data):
    print(name)
    # print(data)

    for i,j in data.items():
        print(i,j)

person('Subhankar', age=30, City='Bangalore', Mob=953555666)

