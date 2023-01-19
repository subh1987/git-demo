num = int(input("Enter the number you want to check prime or not: "))

for i in range(2,num):
    if num % i == 0:
        print("NOT PRIME")
        break
else:
    print("PRIME")
