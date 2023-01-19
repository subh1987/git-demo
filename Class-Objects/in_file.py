from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying file from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print("Is oufile exists ?", exists(to_file))
print("Are you sure yout to copy the files ?")
x = input("PLEASE INPUT YES or NOT ")
prompt = '>'
if (x==YES):
    outfile = open("to_file",'w')
    outfile.writp
else:
    print("EXIT")
outfile.close()
in_file.close()

f = open("to_file", 'r')
print("Goig to print data from destination file")
print(f.read())