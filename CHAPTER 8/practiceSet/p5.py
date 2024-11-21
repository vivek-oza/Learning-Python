# Write a python function to print first n lines of the following pattern: 
# *** 
# **               - for n = 3 
# * 


def printPattern(n):
    if n==0:        #base case, used to exit recursion
        return
    print("*"*n)
    printPattern(n-1)       #recursion


n = int(input("Enter number : "))
printPattern(n)



### USING RECURSION :

def pattern(n):
    if n == 0:
        return
    print("*"*n)
    pattern(n-1)

pattern(n)