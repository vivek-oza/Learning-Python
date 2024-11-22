


class Employee:
    lang= "Py"
    first_salary= "1400000 LPA"


vivekObj = Employee()
vivekObj.name="Vivek"
print(vivekObj.lang, vivekObj.first_salary, vivekObj.name)

avinashObj = Employee()
avinashObj.age=23
print(avinashObj.first_salary, avinashObj.lang,avinashObj.age)




# 1. What happens when you assign harry.name = "Harry"?
# In Python, when you assign harry.name, you're creating an instance attribute dynamically.

# Key Points:
# Python allows objects to have their own attributes, independent of the class.
# When harry.name = "Harry" is executed:
# The name attribute is created dynamically and attached to the harry object.
# This name attribute exists only for that instance (harry) and is stored in its internal __dict__.
# For example:

# harry = Employee()
# harry.name = "Harry"
# print(harry.__dict__)  # Output: {'name': 'Harry'}
# Why does this work?
# Python objects are flexible. You don’t need to predefine attributes in the class; you can add them dynamically to an instance.