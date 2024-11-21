# Write a recursive function to calculate the sum of first n natural num

# def firstNNums(n,i=1):
#     if i>n:
#         return
#     print(i)
#     firstNNums(n-1, i+1)

# n = int(input("Enter number : "))
# print(firstNNums(n))


# def firstNNaturalNums(n,i=1,sum=0):
#     if i > n:       #base case
#         return sum
#     sum+=i      #alternatively, we can directly increment this is recursive call
#     return firstNNaturalNums(n,i+1,sum)     #final value is returned and stored here from base case
    
    

# n = int(input("Enter number : "))
# sum = firstNNaturalNums(n)
# print(f"Sum of first {n} num is {sum}")




### SMART PEOPLES' CODE

def mySum(n):
    if n == 1:
        return 1
    return mySum(n-1) + n


n = int(input("Enter number : "))
sum = mySum(n)
print(f"Sum of first {n} num is {sum}")