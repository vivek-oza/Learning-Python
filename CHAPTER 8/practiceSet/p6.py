# 6. Write a python function which converts inches to cms.
#1 inch is equal to 2.54 centimeters

def lenConverter(n):
    return n*2.54

n = float(input("Enter len in inches : "))

print(lenConverter(n))
