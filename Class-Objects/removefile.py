import os 
x = input("enter the file name you want to delete: ")
print(x)
if os.path.exists("x.txt"):
    os.remove("x.txt")
    print("file has been removed")
else:
    print("file not exists")

# Delete a folder
# os.rmdir("test")
# print("directtory removed")

# os.remove(r"/Users/subhankardas/Downloads/Devops/Python/Class-Objects/sales_2.txt")