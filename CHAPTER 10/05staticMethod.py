
# STATIC METHOD 
# Sometimes we need a function that does not use the self-parameter. We can define a 
# static method like this: 
#
# @staticmethod   # decorator to mark greet as a static method  
# def greet(): 
#     print("Hello user") 




class Employee:
    lang= "Py"
    first_salary= "1400000 LPA"

    def getInfo(this):
        print(f"the language is {this.lang}, the first salary is {this.first_salary}")    
    
    @staticmethod      # decorator to mark greet as static method
    def greet():       
            print("Hello user!")


avi = Employee()
avi.greet()
avi.getInfo()

