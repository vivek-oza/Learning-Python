# # Various methods to perform operation on lists

friends=["apple","orange",45,23.4,False,"Vivek"]
print(friends)


friends.append("Harry")
print(friends)

l1 = [13,45,12,9,4,11,9,6,5]

l1.sort()
l1.sort(reverse=True)
l1.reverse() #this is different from "sort(reverse=True)"
l1.insert(1,9999) #insert 9999 in list l1, such that its index become 1 in list l1
l1.pop(3)
l1.remove(9) #remove first occurence

print(l1)

poppedElement = l1.pop(0)
print(poppedElement)

print(l1)

print(l1.sort())
l1.sort(reverse=True)
print(l1)

# # these list methods have no return value, because they change the original list.
# # whereas in string, there is output as return in string methods