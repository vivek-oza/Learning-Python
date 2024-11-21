a= int(input("Enter a -> "))

#if statement 1 (independent of other)
if(a%2==0):
    print("a is even")

#end if stmt 1


#if statement 2 (independent of other)
if(a<0):
    print("Invalid age")
elif(a>=18):
    print("you are adult")
    print("Enjoy")
elif(a==0):
    print("Youre too young")
else:
    print("Youre not adult")

print("End of program") #Reaches here and ignores other conditions if any exist, or after else that is last


#end if stmt 2