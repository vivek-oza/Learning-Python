# Write a python function to print multiplication table of a given number

def printTable(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

num= int(input("Enter number : "))
printTable(num)