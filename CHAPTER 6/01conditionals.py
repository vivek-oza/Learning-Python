# # CHAPTER  6 – CONDITIONAL EXPRESSION 

# # In python programming too, we must be able to execute instructions on a condition(s) 
# # being met. 
# # This is what conditionals are for!

#

a= int(input("Enter age - "))

# if(a>=18):
#     print("you are adult")
#     print("Enjoy")
# else:
#     print("Youre not adult")


#if elif else ladder

if(a<0):
    print("Invalid age")
elif(a>18):
    print("you are adult")
    print("Enjoy")
elif(a==0):
    print("Youre too young")
else:
    print("Youre not adult")






#     RELATIONAL OPERATORS   for conditions
# Relational Operators are used to evaluate conditions inside the if statements. Some 
# examples of relational operators are: 
# ==: equals. 
# > =: greater than/ equal to. 
# < =: lesser than/ equal to. 
# LOGICAL OPERATORS  
# In python logical operators operate on conditional statements. For Example: 
# • and – true if both operands are true else false. 
# • or – true if at least one operand is true or else false. 
# • not – inverts true to false & false to true



# IMPORTANT NOTES:  
# 1. There can be any number of elif statements. 
# 2. Last else is executed only if all the conditions inside elifs fail. 
  
