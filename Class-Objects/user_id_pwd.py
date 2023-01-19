import getpass

username = input("Enter the user name ")
print(username)

# password = input("Enter the password: ")
# print(password)

# prompt the password with hidden input

password = getpass.getpass("Enter your password")
print(password)


