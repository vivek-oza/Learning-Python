#convert farheneit to celcius
# c/5 = (f-32)/9
# = c = 5*(f-32/)9

f = int(input("Enter farheneit temp : "))
c = 5*(f-32)/9                            #Farheneit temp : 102, celcius temp : 38.888888888888886
print(c)


# f = ((c/5)*9)+32


f = float(input("Enter celcius temp : "))
f = ((f/5)*9)+32                          #Farheneit temp : 102, celcius temp : 38.888888888888886
print(f)

