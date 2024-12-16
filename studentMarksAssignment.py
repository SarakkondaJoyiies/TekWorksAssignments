student_no = input("Enter student number: ")
student_name = input("Enter student name: ")

c_marks = float(input("Enter marks in C: "))
cpp_marks = float(input("Enter marks in C++: "))
java_marks = float(input("Enter marks in Java: "))

total_marks = c_marks + cpp_marks + java_marks
avg_marks = total_marks / 3

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
else:
    grade = 'Fail'

if average_marks >= 70:
    result = 'Pass'
else:
    result = 'Fail'

print("Student Number:",student_no)
print("Student Name:",student_name)
print("Total Marks:",total_marks)
print("Average Marks:",avg_marks)
print("Result:",result)
print("Grade:",grade)