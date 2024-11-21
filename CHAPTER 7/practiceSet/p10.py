# Write a program to print multiplication table of n using for loops in reversed 
# order. 
  
n = int(input("Enter num : "))

for i in range(10,1,-1):
    print(f"{n} x {i} = {n*i}")