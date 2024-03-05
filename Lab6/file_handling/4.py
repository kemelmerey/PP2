#Write a Python program to count the number of lines in a text file.
import os

path = r'C:\Users\Admin\Desktop\PP2_2024\Lab6\file_handling\text.txt'

with open(path, 'r') as f:
	lines = len(f.readlines())
	print(lines)