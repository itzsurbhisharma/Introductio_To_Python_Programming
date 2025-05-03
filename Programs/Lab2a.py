'''Develop a program to generate Fibonacci sequence of 
length (N). Read N from the console.'''

n=int(input("Enter the length of the sequence:"))
f_no=0
s_no=1
print("The Fibbonaci series is:")
print(f_no,s_no,end=" ")

for i in range(2,n+1):
	new_Term=f_no+s_no
	print(new_Term,end=" ")
	f_no=s_no
	s_no=new_Term