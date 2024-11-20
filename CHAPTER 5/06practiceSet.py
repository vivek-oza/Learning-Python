# CHAPTER 5  – PRACTICE SET  

# # 1. Write a program to create a dictionary of Hindi words with values as their English 
# # translation. Provide user with an option to look it up! 

# words= {"madad": "help", "billi":"cat", "kursi":"chair"}
# word = input("Enter word you m=want meaning of : ")
# print(words[word])


# # 2. Write a program to input eight numbers from the user and display all the unique 
# # numbers (once). 
# numSet = set()
# for i in range(8):
#     numSet.add(int(input("Enter a number : ")))

# print(f"All unique nums : {numSet}")


# # 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
# #yes we can have
# s= {1, 2, 18, '18'}
# print(s)


# # 4. What will be the length of following set s: 
# # s = set() 
# # s.add(20) 
# # s.add(20.0) 
# # s.add('20') # length of s after these operations? 
# s= set()
# s.add(20) 
# s.add(20.0) 
# s.add('20')
# print(s) # output = {'20', 20}
# print(len(s)) #output = 2
# ### Because numerically these 2 are equal (2 and 2.0)





# # 5. s = {} 
# #this is dictionary
# s = {} 
# print(type(s))


# # What is the type of 's'? 
# # <class 'dict'>


# # 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# # value and use key as their names. Assume that the names are unique. 

# langs={}

# langs.update({"Vivek":"Java","Saurab":"Python","Achyut":"HTML","Pravesh":"Hindi"})

# print(langs)
# print(langs["Vivek"])


# 7. If the names of 2 friends are same; what will happen to the program in problem 6? 
#dict can have unique key only, so the previos value will be updated in key

# 8. If languages of two friends are same; what will happen to the program in problem 6? 

# # 9. Can you change the values inside a list which is contained in set S?  
# # s = {8, 7, 12, "Harry", [1,2]}
# s = {8, 7, 12, "Vivek", [1,2]} #NOT POSSIBLE
# s.update([1,2],[1,2,3]) #NOT POSSIBLE, WRONG
# print(s) #ERROR

##A LIST CAN NOT BE INCLUDED IN A SET