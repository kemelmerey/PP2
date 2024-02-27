#Write a python program to convert snake case string to camel case string.
import re

txt = input()
txt = txt.title().replace("_", "")
print(txt)