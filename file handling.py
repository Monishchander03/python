###files handling in python
##
###using with read a file
with open ("sample.txt", "r") as file:
    print(file.read())
    
with open ("sample.txt", "r") as file:
    print(file.readline())


with open ("sample.txt", "r") as file:
    print(file.readlines())

#write 
with open ("sample.txt", "a") as file:
    file.write("line1")

with open ("sample.txt", "w") as file:
    file.writelines("\nline1")

#REMOVE
import os
os.remove("sample.text")


Exception handling

try:
    print(x)
except NameError:
    print("x is not defined")
    print("first define a value for x")

    
def my_function(a,b):
    try:
        result = a / b
        return result
    except:
        print("division by zero is not allowed")
print(my_function(10, 2))
print(my_function(5, 0))
    
    

##GREATEST OF TWO NUMBERS   
a = int(input("Enter a number: "))
if a > 0:
    print("The number is positive")
elif a < 0:
     print("The number is negative")
else:
    print("zero")

b = "Hello,World!"
print(b[0:13:-1])


 
