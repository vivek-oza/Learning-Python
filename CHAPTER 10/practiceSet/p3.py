# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

class someClass:
    a= "Microsoft"

o = someClass()

print(o.a) #print clas attr

o.a="Google" #inst attr set

print(o.a) #inst attr printed

print(someClass.a) #class attr not changed
