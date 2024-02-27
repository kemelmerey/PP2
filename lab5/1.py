#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
x = re.findall("ab?", s)
print(x)"""
import re

txt = input()
x = re.findall("ab*", txt)
print(x)