 
# CHAPTER 4 - PRACTICE SET  

# # 1. Write a program to store seven fruits in a list entered by the user. 
# fruits=[]
# for i in range(1,7):
#     fruits.append(input("Enter fruit : "))

# print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner. 
marks=[]
for i in range(1,7):
    mark= input(f"Enter marks in {i} : ")
    marks.append(mark)

marks.sort() #this wont work because, the input data type is string , it will sort marks alphabetically
print(marks)


# change the input datatype to integer
for i in range(1,7):
    mark= int(input(f"Enter marks in {i} : "))
    marks.append(mark)

marks.sort() #this wont work because, the input data type is string
print(marks)





# 3. Check that a tuple type cannot be changed in python. 
# tuple cant be changed, meaning its immutable


# 4. Write a program to sum a list with 4 numbers. 

list1=[1,5,2,4]
print(sum(list1))
print(sorted(list1))

# 5. Write a program to count the number of zeros in the following tuple: 
# a = (7, 0, 8, 0, 0, 9)

tuple_a = (7, 0, 8, 0, 0, 9)
print(tuple_a.count(0))