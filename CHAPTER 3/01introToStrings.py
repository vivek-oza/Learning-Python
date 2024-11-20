
#string a data type 
#a sequence of characters
#can be made using 3 ways ', ", """
#string is immutable

#index -> start from 0 to len-1 , also from -1 when in reverse

name = "coding's cool, coding school"
print(name)

print(name[2])
print(name[-4])

#f strings

name= input("Enter name : ")
date= input("Enter date : ")
print(f'''
Dear {name} You are Selected! {date}
''')


#string slicing

nameSubStr = name[0:6] #from index 2 till 5, excluding 5
print(nameSubStr)

