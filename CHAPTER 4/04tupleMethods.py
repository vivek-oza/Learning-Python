
tup = (1, 2, 35.3, False, 2,"Vivek", 2, "Harry")
t2 = (45,2,1,4,5,3)
print(tup)

# Since tuple is alos immutable like string and not like list, hence the original tuple can tbe changed, and the methods return the changed tuple on which operation is performed
# original tuple remains unchanged

# Methods 

print(tup.count(2))

print(tup.index(False))

print(tup.index(2))

# Tuples support indexing, slicing, concatenation, repetition, iteration, and various utility operations like len(), count(), and index().
# While tuples are immutable, operations like sorting or modification require creating new tuples.

print(2 in tup)
print(len(tup))

print(tup+t2)

print(t2*2)
print(sorted(t2))
