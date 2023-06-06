#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0: #checks if number is greater 0
	print("{} is a positive".format(number))
elif number == 0:
	print("{} is zero".format(number))
else:
print("{} is negative".format(number))
