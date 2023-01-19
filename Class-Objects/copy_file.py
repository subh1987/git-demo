from sys import argv
from os.path import exists

from_file = input("Enter the source file: ")
source_file = open("from_file", 'r')
indata = source_file.read()


to_file = input("Enter the Target file name: ")
print(f"is destination file exists ? {exists(to_file)}")
destination_file = open("to_file", 'w')
destination_file.write(indata)

destination_file.close()
source_file.close()

checkfiles = open("to_file", 'r')
print(checkfiles.read())
checkfiles.close()
# out_file = input("Enter the File name: ")

# file = open(r"/Users/subhankardas/Downloads/Devops/Python/Class-Objects/Test.txt",'w')

# file1 = input("Line1: ")
# file.write(file1)
# file.close()

# # check if the line has been added to the file or not

# file2 = open(r"/Users/subhankardas/Downloads/Devops/Python/Class-Objects/Test.txt",'r')
# print("Reading the contect of the file: -------------")
# print(file2.read())
# file2.close