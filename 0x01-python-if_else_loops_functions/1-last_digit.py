#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number > 5:
    print("Last digit of {} is {} and is greater than 5". format(number, last))
elif number == 0:
    print("Last digit of {} is {} and is 0". format(number, last))
else:
    print("Last digit of {} is {} and is less than 6". format(number, last))
                                          