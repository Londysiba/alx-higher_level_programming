#!/usr/bin/python3
def uppercase(string):
    for character in string:
        if "a" <= character <= "z":
            uppercase_char = chr(ord(character) - 32)
            print(uppercase_char, end="")
        else:
            print(character, end="")
    print()
