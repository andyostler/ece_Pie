from math import *

def pyramid(s):
	"""Prints a 'message pyramid' for the input message string"""
	out=''
	for arg in s:
		out+=arg
		print(out)

def findsquares(s:int, e:int):
	squares = []
	if s > e:
		start = e
		end = s
	else:
		start = s
		end = e

	for i in range(start, end+1):
		if (int(sqrt(i))*int(sqrt(i))) == i:
			squares.append(i)
	return squares

def calSalary(h:float, r:float=20):
	if h <= 0:
		print("Not Valid Hours")
		return -1
	elif h > 40:
		overtime = h-40
	else:
		overtime = 0
	return ((r*h) + (overtime * 1.2*r))

def calLetterGrade(points:float, gradescale:list):
	length = len(gradescale)
	grade = ["A+", "A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]
	if length > 12:
		print("Invalid list")
		return -1

	for i in range(length):
		if (type(gradescale[i])!=int) & (type(gradescale[i])!=float):
			print("Invalid list")
			return -1
		elif i == (length-1):
			return "F"
		elif gradescale[i] == gradescale[i+1]:
			print("Repeated Entries")
			return -1
		elif points >= gradescale[i]:
			return grade[i]

