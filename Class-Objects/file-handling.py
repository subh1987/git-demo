## Open a file name and read the content of the fle ##

# file = input("Enter the file name: ")

# txt_file = open(file)

# print(txt_file.read())

# txt_file = open(file)
# txt_file.write


## Open a file and Write some lines into it 
from sys import argv

filename = input("Enter the file name: ")

print(f"We are going to add line to the {filename} ")
target = open(filename, 'w') # open file in write mode

target.truncate()


print("Now I'm going to ask you for three lines. ")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I'm going to write these to the file: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("finally we close the file")

target.close()


