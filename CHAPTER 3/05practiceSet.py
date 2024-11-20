# # 1. Write a python program to display a user entered name followed by Good 
# # Afternoon using input () function. 

# name = input("Enter name : ")
# print(f" Good afternoon {name}")


# # 2. Write a program to fill in a letter template given below with name and date. 
# # letter = '''  
# #        Dear <|Name|>, 
# #        You are selected! 
# #        <|Date|> 
# #         ''' 
 
# name= input("Enter name : ")
# date= input("Enter date : ")
# print(f'''
# Dear {name} You are Selected! {date}
# ''')

# name= input("Enter name : ")
# date= input("Enter date : ")
# letter='''
# Dear <|Name|>, 
# You are selected! 
# <|Date|>
# '''
# print(letter.replace('<|Name|>',name).replace("<|Date|>",date))




# # 3. Write a program to detect double space in a string.  

# str = "Vivek is a good  boy "
# str2 = "This is a string without double space"
# print(str.find("  "))
# print(str2.find("  "))




# # 4. Replace the double space from problem 3 with single spaces.

# print(str.replace("  "," "))

# print(str) #strings are immutable, cant be changed




# 5. Write a program to format the following letter using escape sequence 
# characters. 

letter = "Dear Harry, this python course is nice. Thanks!"

print(letter)

print("Dear Harry,\n\tThis python course is nice.\nThanks!")