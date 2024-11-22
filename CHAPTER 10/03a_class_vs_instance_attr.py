class Employee:
    lang= "Py"  #tis is class atribute
    first_salary= "1400000 LPA"


vivekObj = Employee()
vivekObj.name="Vivek" #tis is instance atribute
print(vivekObj.lang, vivekObj.first_salary, vivekObj.name)



avinashObj = Employee()
avinashObj.age=23 #tis is instance atribute
print(avinashObj.first_salary, avinashObj.lang,avinashObj.age)


# here, salary and language are Class attribute (directly belong to class)
# here "name" and "age" are object attribute

#objects can have independent attributes in python, unlike JAVA





#### INSTANCE ATTR

# instanc attribute take preference over class attribute during assignment and retrieval

class Employee:
    lang= "Py"  #tis is class atribute
    first_salary= "1400000 LPA"


vivekObj2 = Employee()
vivekObj2.lang="JavaScript" #tis is instance atribute, it takes preference over class attributes
print(vivekObj2.lang, vivekObj2.first_salary)











# Note: Instance attributes, take preference over class attributes during assignment & 
# retrieval. 
# When looking up for harry.attribute it checks for the following: 
# 1) Is attribute present in object? 
# 2) Is attribute present in class?