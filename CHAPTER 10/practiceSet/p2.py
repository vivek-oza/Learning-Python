# Write a class “Calculator” capable of finding square, cube and square root of a number.

from math import sqrt

class Calc:

    def __init__(self,n):
        self.n= n

    def sq(self):
        print( "Squarw",self.n**2 )

    def cb(self):
        print( "Cube",self.n**3 )

    def sqroot(self):
        print( "Squarw root",sqrt(self.n) )
        print( "Squarw root",self.n**1/2 )


    @staticmethod
    def greet():
        print("Hello user")



num = Calc(5)
num.sq()
num.cb()
num.sqroot()   

num.greet()