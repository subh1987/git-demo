# class computer:

#     def config(self):
#         print("i5, 16gb, 1TB")

# # x = "7"
# # print(type(7))
# # a = 8
# # print(type(a))

# com1 = computer()
# com2 = computer()
# com1.config()
# computer.config(com2)
# computer.config(com1)



# my_name = 'subhankar das'
# my_age = 30
# my_height = 85 #Inches

# print(f"Lets talk about {my_name}.")
# print(f"my age is {my_age}")
# print(f"my height is {my_height}")
# print('subh')
# print("subhankar das")

# types_of_people = 10
# print(f"There are {types_of_people} people exists")

# w = "This is the left side of ... "
# e = "a string with the right side .. "

# print(w+e)

# print("The lamb is whie as {}. ".format("snow"))

# a = "C"
# b = "H"
# c = "O"
# d = "R"

# print(a+b+c+d, end='')

# print("." *10)


# formtter = "{} {} {} {}"
# print(formtter.format(1,2,3,4))
# print(formtter.format("one", "two", "three", "four"))
# print(formtter.format("Try your code", "Hello from code", "congrats",  "your first code"))


# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMarch\nApril\nMay\June"
# print("These are the days", days)
# print("The months are", months)

# tabby_cat = "\tI'm tabbed in."
# print(tabby_cat)

# persian_cat = "I'm split\non a line\nShut."
# print(persian_cat)

# backslash_cat = "I'm \\ a \\ cat"
# print(backslash_cat)

# print("How old are you ? ", end=' ')  # end = continue is single line
# age = input()

# print("How tall are you? ", end=' ')
# height = input()

# print(f"So, you are {age} old, {height} tall")

# from sys import argv
# # read the WYSS section for how to run this
# script, first, second, third = argv
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)
# x = input("your name:- ")
# print(x)

# from sys import argv

# script, user_name = argv

# print(f"Hi {user_name}, I'm the {script} script. ")
# print(f"Do you like me {user_name}?")
# prompt = '>'
# likes = input(prompt)

# print(f"Where do you lives {user_name}? ")
# lives = input(prompt)

# print(f"Alright, so {user_name} said {likes} about liking me and you lives in {lives} ")


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

