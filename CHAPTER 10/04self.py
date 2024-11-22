
# # class Employee:
# #     lang= "Py"
# #     first_salary= "1400000 LPA"

# #     def getInfo(self):
# #         print(f"the language is {self.lang}, the first salary is {self.first_salary}")


# # vivekObj = Employee()

# # vivekObj.getInfo()

#This code will give an error that we are passing 1 argument in getInfo() function, when we are not passing it.

#error : 
# TypeError: Employee.getInfo() takes 0 positional argumTypeError: Employee.getInfo() takes 0 positional arguments but 1 was given


'''
because when  -> #vivek.getInfo() 
is called, it got called like this -> #Employee.getInfo(vivek)

actually it is automatically converted into the latter syntax, or we can directly call it like that, 
and to solve this error, we give methods, a keyword that points to current object, generally "self" in python 
and syntactically it is like "this" in java

"self" is necessary for making a function, doesnt matter if we use it or not

THIS CAN BE RESOLVED FOR SIMPLE FUNCTIONS WHEN NO PARAMS OR PROPERTY NEEDED FROM AN OBJECT WHEN DOING THIS FUNCTION CALL, THAT IS(ie), USING
"" STATIC METHODS  ""

'''










# #### SELF in python IS LIKE "this" in JAVA, it points to the current object which is refering to the function and using it
# ##### I MEAN,  """" THE KEYWORD CAN BE WRITTEN ANYTHING """" BUT, the general convention is writing "self" for this PURPOSE in PYTHON


class Employee:
    lang= "Py"
    first_salary= "1400000 LPA"

    def getInfo(self):
        print(f"the language is {self.lang}, the first salary is {self.first_salary}")


vivekObj = Employee()

vivekObj.name="Vivek"

vivekObj.getInfo()
#OR
Employee.getInfo(vivekObj)








# ## using "this", just for satisfaction and verification:
class Employee:
    lang= "Py"
    first_salary= "1400000 LPA"

    def getInfo(this):
        print(f"the language is {this.lang}, the first salary is {this.first_salary}")


vivekObj = Employee()

vivekObj.name="Vivek"

print(vivekObj.lang, vivekObj.first_salary, vivekObj.name)

vivekObj.getInfo()




# "self" is necessary for making a function, doesnt matter if we use it or not

# # Example
class Employee:
    lang= "Py"
    first_salary= "1400000 LPA"

    def getInfo(self):
        print(f"the language is {self.lang}, the first salary is {self.first_salary}")
    
    def greet(self):
        print("Hello")


vivekObj = Employee()

vivekObj.greet()


# SELF PARAMETER   
# self refers to the instance of the class. It is automatically passed with a function call from an object


### THIS CAN BE RESOLVED FOR SIMPLE FUNCTIONS THAT DONT NEED PRARMETERS FROM THE OBJECT USING "static methods" ###