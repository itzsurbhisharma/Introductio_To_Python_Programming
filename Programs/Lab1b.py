'''Develop a program to read the name and year of 
birth of a person. Display whether the person is a
senior citizen or not.'''

name=input("Enter you name:")
yearOfBirth=int(input("Enter the year of your birth:"))
currentYear=int(input("Enter the current year:"))
age=currentYear-yearOfBirth

if age>60:
	print(name,"you are",age,"years old. You are a senior citizen.")
else:
	print(name,"you are",age,"years old. You are not a senior citizen.")