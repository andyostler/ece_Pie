"""This script takes a valid, non-zero value for height in feet and weight \
in lbs and calculates a Body Mass Index(BMI)"""
weight = input("Give in a valid weight in lbs:")
height = input("Give in a valid height in feet:")

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
print("Weight = {:.3f} lbs = {:.3f} kg\n".format(weight, kg))
print("Height = {:.3f} feet = {:.3f} meters\n".format(height, meters))
print("BMI = {:.3f}".format(BMI))
