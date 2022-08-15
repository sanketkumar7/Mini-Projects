import math
n=int(input("Enter the no of students..: "))
d={}
for i in range(n):
	name=input("Please enter the Name : ")
	marks=int(input(f'{name}, please enter the marks : '))
	d[name]=marks
	if i!=n-1: print(f'{i+1} students data inserted.')
print('All Students data inserted successfully')
print('*'*30,'\n\tStudent Record\n','*'*30)
print('\t Name\t\tMarks')
for k,v in d.items():
	print(f'\t{k}\t-\t{v}')
print('*'*30)
print('Searching records')
while True:
	name=input("Please Enter your name :").title()
	marks=d.get(name,-1)
	if marks==-1:
		print(f"{name} Student Not Found")
	else:
		print(f'{name} has {marks} marks')
	option=input('Do you want to find another student marks[Yes|No]')
	if option.lower()=='no':
		break
print('Thank you for using our small Application.')