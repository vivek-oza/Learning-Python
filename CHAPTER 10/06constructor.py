# __INIT__() CONSTRUCTOR 
# __init__() is a special method which is first run as soon as the object is created. 
# __init__() method is also known as constructor. 
# It takes ‘self’ argument and can also take further arguments.


class Employee:
    lang= "Python"
    salary= "1400000 LPA"

    def __init__(self, name, salary, lang):     ## a dunder method, the __init__() dunder method is automatically called
         print("Creating an object")         
         self.name=name
         self.salary=salary
         self.lang=lang

    def getInfo(self):
        print(f"the language is {self.lang}, first salary is {self.salary} and Employee is {self.name}")    
    
    @staticmethod      # decorator to mark greet as static method
    def greet():       
            print("Hello user!")



# 
# someEmployee = Employee()

someEmployee = Employee("Vivek",1600000,"JavaScript")

someEmployee.greet()
someEmployee.getInfo()



