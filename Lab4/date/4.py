#Write a Python program to calculate two date difference in seconds.

import datetime

x = datetime.datetime.now()
y = datetime.datetime(2024, 2, 16, 11)
print(x - y)


print((x-y).total_seconds())