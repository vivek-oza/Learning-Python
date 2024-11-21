# CHAPTER 6 – PRACTICE SET  



# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 


passingSubject= 33
passingOverall= 40
marks= []
subjectResult= []

for i in range(3):
    x=i+1
    m= int(input(f"Enter marks in {x} -> "))
    marks.append(m)

print(marks)

for mark in marks:
    if mark >= passingSubject:
        subjectResult.append("Pass")
    else:
        subjectResult.append("Fail")

print(f"Subject wise result -> {subjectResult}")

marksObtained= sum(marks)
print(f"Total marks obtained -> {marksObtained}")

if marksObtained/3 >= 40:

    if "Fail" not in subjectResult:
        print(f"Student passed, percentage obtained -> {marksObtained/3}%")
    elif "Fail" in subjectResult:
        print(f"Student not passed in one or more subject, percentage obtained -> {marksObtained/3}%")

else:
    print(f"Student Failed,overall percentage note more than 40. percentage obtained -> {marksObtained/3}%")


###this one is not that good



# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 




# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 




# 5. Write a program which finds out whether a given name is present in a list or not. 




# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        => F 




# 7. Write a program to find out whether a given post is talking about “Harry” or not. 
 