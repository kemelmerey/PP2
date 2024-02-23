#Write a Python program to calculate the area of regular polygon.

import math

print("Input number of sides: ")
n = int(input())

print("Input the length of a side: ")
l = int(input())

P = n * l

a = 2 * math.tan((180/n)*(3.14/180))
b = l/a
A = n * l * b * (1/2)

print("The area of the polygon is: ", int(A))