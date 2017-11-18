##String calculator challenge

##Write a program which takes a string of user input and treats it as a mathematical calculation, reporting the result of the calculation to the user.

##Support addition, subtraction, multiplication and division represented by “+”, “-“, “*”, and “/”
##Unrecognised numbers should result in an error being reported to the user, indicating the string which was not recognised

from sys import argv

def Checking(a,b,c):
	validation = True
	try:
		int(a)
	except ValueError:
		print('Error. Unrecognised number',a)
		validation = False
	try:
		int(c)
	except ValueError:
		print('Error. Unrecognised number',c)
		validation = False
	operation_list = ['+','-','*','/','**']
	if b not in operation_list:
		print('Error. Unrecognised operation',b)
		validation = False
	return validation

def Operation(a,b,c):
	answer = 0
	if b == '+':
		answer = int(a) + int(c)
		print(instruction, 'is', answer)
	elif b == '-':
		answer = int(a) - int(c)
		print(instruction, 'is', answer)
	elif b == '*':
		answer = int(a) * int(c)
		print(instruction, 'is', answer)
	elif b == '/':
		answer = int(a) / int(c)
		if int(a) % int(c) == 0:
			print(instruction, 'is', int(answer)) #returns integer
		else:		
			print(instruction, 'is', answer) #returns decimals
	elif b == '**':
		answer = int(a) ** int(c)
		print(instruction, 'is', answer)	

script, instruction = argv 
#argv - taking input when first launch program
#script-name of file, instruction must be ONE thing (do item1,item2 etc if more than 1 a,b,c = instruction.split(' ')
a,b,c = instruction.split(' ')

if Checking(a,b,c):
	Operation(a,b,c)