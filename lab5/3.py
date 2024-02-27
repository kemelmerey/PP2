#Write a Python program to find sequences of lowercase letters joined with a underscore.
"""import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
x = re.findall("^[a-z]+_[a-z]+$", s)
print(x)"""
import re
txt = input()
x = re.findall("[a-z]+_[a-z]+", txt)
print(x)