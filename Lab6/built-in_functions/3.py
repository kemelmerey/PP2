# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

txt = input("Enter a string: ")
palidrom_check = txt[::-1]

d = False
for i in palidrom_check:
    if i.isalnum():
        d = True
    else:
        d = False 
if palidrom_check == txt and d:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")