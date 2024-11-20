# CHAPTER 5 – DICTIONARY & SETS

# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs

# “key” : value

# They are unordered, mutable(changeable) & don’t allow duplicate keys


d={} #Empty dictionary , and not an empty set


marksDict = {
    "Vivek": 100,
    "Saurav": 90,
    "Achyut":55,
    0:"Pravesh"
}
print(marksDict)
print(type(marksDict))

# Cant do indexing by number implicitly, we can use either integers or strings explicitly for indexing , print(marks[0])
#instead we can do use keys to access values

print(marksDict["Vivek"])

#properties
#1. Unordered
#2. Mutable
#3. Indexed
#4. Cant have duplicate keys

a= {
    "key": "Value",
    "name": "Vivek",
    "marks": 100,
    "list": [1,3,4.5]
}



