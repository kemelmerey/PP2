#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
"""import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
x = re.findall("ab{2,3}?", s)
print(x)"""
import re

txt = input()
x = re.findall("ab{2,3}", txt)
print(x)