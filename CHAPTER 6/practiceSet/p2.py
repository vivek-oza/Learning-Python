
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









###improved version





# Criteria for passing
passingSubject = 33  # Marks needed in each subject
passingOverall = 40  # Overall percentage needed

# List to store marks of three subjects
marks = []

# Ask the user to enter marks for 3 subjects
for i in range(3):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Calculate the total marks and percentage
totalMarks = sum(marks)
percentage = totalMarks / 3

# Check if the student passed in each subject
passedAllSubjects = True
for mark in marks:
    if mark < passingSubject:
        passedAllSubjects = False
        break

# Final Result
print(f"Marks: {marks}")
print(f"Total Marks: {totalMarks}")
print(f"Percentage: {percentage:.2f}%")

if passedAllSubjects and percentage >= passingOverall:
    print("Congratulations! You passed!")
else:
    print("Sorry, you failed.")
    if not passedAllSubjects:
        print("Reason: You failed in one or more subjects.")
    if percentage < passingOverall:
        print("Reason: Your overall percentage is below 40%.")









###better improved version



# Passing criteria
passingSubject = 33
passingOverall = 40

# Store marks and results
marks = []
subjectResult = []

# Input marks for 3 subjects
for i in range(3):
    m = int(input(f"Enter marks in subject {i + 1}: "))
    marks.append(m)

# Check subject-wise results
for mark in marks:
    if mark >= passingSubject:
        subjectResult.append("Pass")
    else:
        subjectResult.append("Fail")

# Calculate total marks and percentage
totalMarks = sum(marks)
percentage = totalMarks / 3

# Print results
print(f"Marks: {marks}")
print(f"Subject-wise result: {subjectResult}")
print(f"Total Marks: {totalMarks}")
print(f"Percentage: {percentage:.2f}%")

# Final decision
if percentage >= passingOverall and "Fail" not in subjectResult:
    print("Student passed! Congratulations!")
else:
    print("Student failed.")
    if "Fail" in subjectResult:
        failedSubjects = [i + 1 for i, result in enumerate(subjectResult) if result == "Fail"]
        print(f"Reason: Failed in subject(s): {failedSubjects}.")
    if percentage < passingOverall:
        print("Reason: Overall percentage is below 40%.")









####  BETTER THAN ALL OF THIS IS KEEP PROGRAM SIMPLE AND USE "and" IN CONDITIONAL CHECKING IN IF CONDITIONS ###