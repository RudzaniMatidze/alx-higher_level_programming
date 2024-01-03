#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
thestring = "Last digit of {} is {}".format(number, digit)
if digit > 5:
    print(f"{thestring} and is greater than 5")
elif digit == 0:
    print(f"{thestring} and is 0")
elif digit < 6:
    print(f"{thestring} and is less that 6 and not 0")
