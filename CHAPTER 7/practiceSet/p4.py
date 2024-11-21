# 4. Write a program to find whether a given number is prime or not


n= int(input("Enter n : "))

for i in range(2, n):
    if(n%i) == 0:
        print("Not prime")
        break
else:
    print("Prime")


#USE OF FOR LOOP WITH OPTIONAL ELSE