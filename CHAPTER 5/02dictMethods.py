##Methods on dictionary


marksDict = {
    "Vivek": 100,
    "Saurav": 90,
    "Achyut":55,
    "Pravesh":0
}

print(len(marksDict))

print(marksDict.items()) #gives key val pairs in tuple
print(marksDict.keys()) #gives key 
print(marksDict.values()) #gives values

marksDict.update({"Vivek":99}) #Mutablity, update value
print(marksDict) #gives values


marksDict.update({"Jiya":100}) #Mutablity, added an item
print(marksDict) #gives values


print(marksDict.get("Kisna")) #gives none
print(marksDict.get("Vivek")) #gives values

# #Difference b/w get() and direct access
# print(marksDict.get("Vivek2")) #Prints NONE
# print(marksDict["Vivek2"]) #Returns an ERROR

#POP remove specified element and return the value
print(marksDict.pop("Pravesh","default value when error")) #pops key value and gives values
print(marksDict)

# marksDict.clear()
# print(marksDict) #Purges all items from dictionary


# #POPITEM remove element and return the key value pair in LIFO manner
# print(marksDict.popitem()) #pops key value and gives key value pair
# print(marksDict)