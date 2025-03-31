student_name=input("Enter the name of the student: ")

student_usn=input("Enter the usn of the student: ")

print("Enter the marks of three subjects:")
m1=float(input("Enter the marks of subject 1: "))
m2=float(input("Enter the marks of subject 2: "))
m3=float(input("Enter the marks of subject 3: "))

total_marks=m1+m2+m3
percentage=total_marks/3

print("Student's Name: ",student_name)
print("Student's USN: ",student_usn)
print("Student's Total Marks: ",total_marks)
print("Student's Percentage: ",percentage)
