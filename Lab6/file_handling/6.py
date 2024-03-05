#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os

path = r"C:\Users\Admin\Desktop\PP2_2024\Lab6\file_handling\files_from_6ex"

for i in range(65,91):
    name = os.path.join(path, chr(i) + ".txt")
    f = open(name, "a")