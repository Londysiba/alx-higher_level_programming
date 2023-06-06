#!/usr/bin/python3
for digits in range(0, 10):
    for digits1 in range(digits + 1, 10):
        if digits == 8 and digits1 == 9:
            print("{}{}".format(digits, digits1))
        else:
            print("{}{}".format(digits, digits1), end=", ")
