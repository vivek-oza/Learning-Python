# CHAPTER 8  – PRACTICE SET  
# 1. Write a program using functions to find greatest of three numbers.

# def greatestNumSmart(nums):
#     return max(nums)


# nums= []
# for i in range(3):
#     num = int(input("Enter num1 : "))
#     nums.append(num)

# print(greatestNumSmart(nums))


def greatestNumDumb(a,b,c):
    if(a>b & a>c):
        return a
    elif(b>a & b>c):
        return b
    elif(c>a & c>b):
        return c
    elif(a == b == c):
        return "All are equal"
    

print(greatestNumDumb(4,45,2))
print(greatestNumDumb(2,2,2))