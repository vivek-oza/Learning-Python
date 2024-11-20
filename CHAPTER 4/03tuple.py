#Tuple is an immutable type of collectoin data type that can store any data type.

tup= (1,34,2,3,5,64)
print(type(tup))

a= ()  #Empty tuple
print(type(a))

a= (1)
print(type(a)) #type is int, but we want single element tup

a= (1,) #SIngle element tuple
print(type(a))

tup = (1,2,35.3,False, "Vivek", "Harry")
print(tup)