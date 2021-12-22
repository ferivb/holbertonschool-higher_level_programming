#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    ldigit = (number % -10)

else:
    ldigit = (number % 10)

print('Last digit of {} is {} and is '.format(number, ldigit), end="")

if (ldigit == 0):
    print('0')

elif (ldigit < 6):
    print('less than 6 and not 0')

else:
    print('greater than 5')
