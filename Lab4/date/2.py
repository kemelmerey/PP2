#Write a Python program to print yesterday, today, tomorrow.
import datetime

today = datetime.datetime.now()
yesterday = today.day - 1
d2 = datetime.date(today.year, today.month, yesterday)
print(d2)

today = datetime.datetime.now()
print(today)

tomorrow = today.day + 1
d3 = datetime.date(today.year, today.month, tomorrow)
print(d3)