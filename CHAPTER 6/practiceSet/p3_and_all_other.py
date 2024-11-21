
# # 3. A spam comment is defined as a text containing following keywords: 
# # “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# # to detect these spams. 

#using "in"





# # 4. Write a program to find whether a given username contains less than 10 
# # characters or not. 

# username = "vivek-oza"
# if len(username) < 10:
#     print(f"usrnm {username}, has lessthan 10 chars")


# #5. Write a program which finds out whether a given name is present in a list or not. 

#using "in"


# # 6. Write a program to calculate the grade of a student from his marks from the 
# # following scheme: 
# # 90 – 100 => Ex 
# # 80 – 90 => A 
# # 70 – 80 => B 
# # 60 – 70  =>C 
# # 50 – 60 => D 
# # <50        => F 

# using if elif ladder






# 7. Write a program to find out whether a given post is talking about "Vivek" or not. 


post= input("Enter post : ")

if "vivek" in post.lower():
    print("Post talking about vivek")
else:
    print("Post NOT talking about vivek")

