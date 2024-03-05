#Write a Python program to write a list to a file.
import os

list = ["apple", "melon", "lemon"]

with open("C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6\\file_handling\\dir.txt", "w") as file:
    for i in list:
        file.write(i + "\n")