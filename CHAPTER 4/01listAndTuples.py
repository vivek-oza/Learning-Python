# CHAPTER 4 – LISTS AND TUPLES  

# Python lists are containers to store a set of values of any data type, we can store diffrent type of data
#list are mutable type of collection data type

friends=["apple","orange",45,23.4,False,"Vivek"]
print(friends)
print(friends[0:3])
print(friends[1])

### STRINGS ARE NOT MUTABLE
### LISTS ARE MUTABLE

friends[1] = "grapes"
print(friends)

# Lists has indexing, start from ZERO

# List slicing
print(friends[0:3])
print(friends[3:])


print(type(friends))

