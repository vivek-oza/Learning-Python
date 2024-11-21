# 1. Write a program to find the greatest of four numbers entered by the user. 
nums=[]
for i in range(4):
    x=i+1
    n= int(input(f"Enter number {x} -> "))
    nums.append(n)

print(nums)
print(f"Max of all is : {max(nums)}")

