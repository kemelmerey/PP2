#Write a Python program to subtract five days from current date.
import datetime 

x = datetime.datetime.now()
print(x)

y = x.day - 5
x2 = datetime.date(x.year, x.month, y)
print(x2)