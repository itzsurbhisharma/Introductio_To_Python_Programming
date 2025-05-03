'''Read N numbers from the console and create a list. Develop a program to print mean, 
variance and standard deviation with suitable messages.'''

n=[]
size=int(input("Enter the number of elements"))

for i in range(0,size):
	str=int(input("Enter the elements:"))
	n=n+[str]

total=0
for ele in n:
	total+=ele

mean=total/size
print("Mean is:",mean)

total=0
for ele in n:
	total+=(ele-mean)**2

var=total/size
print("Variance is:",var)

std=(var)**(1/2)
print("Standard Deviation is:",std)


