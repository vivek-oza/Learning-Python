# Write a program to print the following star pattern. 
#   * 
#  *** 
# *****  for n = 3 

'''
  *
 ***
*****
'''

#hint = you will have to use odd number series to print stars, and decreing order to priont spaces

n= int(input("Enter n "))

for i in range(1, n+1):
    print(" "*(n-i), end="" )
    print("*"*(2*i-1), end="")
    print("")
