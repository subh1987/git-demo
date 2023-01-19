# a = 20

# def variable():
#     a = 15
#     print("Value from local", a)
# variable()
# print("Value from global", a)

a = 20  # Global variable

def variable():
    global a        # local but decalred global, it will be as a globAL
    a = 15
    print("Value from local", a)
variable()
print("Value from global", a)



