
# CHAPTER 10 – PRACTICE SET  
# 1. Create a class “Programmer” for storing information 
# of few programmers working at Microsoft

class Programmer:
    company= "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin=pin
    def getInfo(self):
        print(f"Employee at: {self.company} \n Name: {self.name} \n Salary: {self.salary} \n PIN: {self.pin} ")

v14260 = Programmer("Vivek",2400000,382123)
v14260.getInfo()

r1234 = Programmer("Rohan",1400000,782123)
r1234.getInfo()