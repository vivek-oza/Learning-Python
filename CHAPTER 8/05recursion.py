# RECURSION  
# Recursion is a function which calls itself. 
#RECURSION AND LOOPS ARE RELATED
#RECURSION CAN DO EVERYTHING THAT LOOPS DO vice-versa
# It can be used to directly use a mathematical formula as function. 

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(5) #5 = n , 4 = n-1 ,3= n-2, 2= n-3, 1 = n-4

# #recursion
# ## kaam likho
# ## then dekho ki next kaam kaise hoga
# ##  (base case) use return empty to return control to normal flow0
# # (base case) -> jo recursion ko rok de


# #Recursice Functions Have -> call stack. these go till the last task and then in LIFO manner traverse function call stack, and  if all lines are executed then continue traverse, but if any line is remaining then execute it, example, here printing END was remaining in all lines, so they print at last

# #base case is needed to exit the infinite function calls



# # Reccurence -> badi ciz ka chota version aa rha hai, then we can use recursion

#FACTORIAL

n=int(input("Enter n : "))
fact= 1

def fact(n):
    if fact == 0 or fact ==1:
        return
    fact = fact(n-1)*fact






# ## THIS IS TRASH CODE, NEVER DO THIS

# def factorialFun(n):
#     fact=1
#     if(n==1 or n==0):
#         return 1
#     fact= n * factorialFun(n-1)
#     return fact

# n= int(input("Enter number for fatorial : "))

# print(factorialFun(n))




### GOOD CODE, COPIED FROM GPT

def factorialFun(n):
    if n == 1 or n == 0:  # Base case: factorial of 0 or 1 is 1
        return 1
    return n * factorialFun(n - 1)  # Recursive call to calculate factorial

# Input and output
n = int(input("Enter number for factorial: "))
print(f"The factorial of {n} is: {factorialFun(n)}")







#### ALSO GOOD CODE, AFTER DOING THIS SIMPLE THING FOR MORE THAN AN HOUR, I GOT IT RIGHT, I AM PROUD OF ME, THANKS, AND i KNOW i WILL MAKE IT TO SOME BIG TECH SOON ENOUGH



def factFun(n):
    if n==1 or n==0:
        return 1
    fact= n * factFun(n-1)
    return fact

num = int(input("Enter number : "))
print(factFun(num))

