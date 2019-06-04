"""This script takes a valid, non-zero value for height in feet and weight \
in lbs and calculates a Body Mass Index(BMI)"""
import Homework2

name = input("What is your name:")
weight = input("What is your weight in lbs?")
height = input("What is your height in feet?")

try:
	weight = float(weight)
	kg = weight*0.453592
except TypeError:
	print("Non-numeric weight")
try: 
	height = float(height)
	meters = height*0.3048
except TypeError:
	print("Non-numeric height")

try:
	if (kg!=0):
		BMI = kg/(meters**2)
	else:
		print("Invalid weight")
		exit()
except ZeroDivisionError:
	print("Invalid height")
	exit()
Homework2.dataRecorder("patient_records.csv", {"Name": name, "Weight": weight, "Height":height})
