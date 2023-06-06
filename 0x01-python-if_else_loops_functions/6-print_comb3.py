#!/usr/bin/python3
for digit1 in range(0, 10):
    for digits2 in range(digit1 + 1, 10):
        if digit1 == 8 and digits2 == 9:
            print("{}{}".format(digit1, digits2))
        else:
            print("{}{}".format(digit1, digits2), end=", ")
