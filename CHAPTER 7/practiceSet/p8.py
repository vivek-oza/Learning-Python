# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 


n= int(input("Enter n "))

for i in range(1, n+1):
    print("*"*i, end="")
    print("")