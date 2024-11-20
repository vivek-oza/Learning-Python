#Set , like in maths , class 12 maths chapter 1.

#Set in Python

# Set is the collection of the unordered items data type.
# Can store diffrent data types
#Sets are NOT indexed => cant access by indexing
# Each element in the set must be unique
# Set is immutable.

e= set() #Empty set , Dont use s={}, as it will create empty dictoinary 

s={1,2,1,43,23,5,6,7,7,7} #Unordered and Non repetetive elements
print(s)
print(type(s))

s2= {12, "Vivek", 10, 99.5, True}
print(s2)
print(type(s2))


#properties
#unordered
#no way to change items
#means, it is immutable
#Sets are NOT indexed



#SPECIAL CASE -> Look it up on chat gpt too
# in python , 1.0 == 1 , returns true, because it doesnt check datatype if the actual data is Numerically equal.
#look at the practice set question 5 of this chapter and if needed then code wit harry full python course too.

#SPECIAL CASE 
##A LIST CAN NOT BE INCLUDED IN A SET
