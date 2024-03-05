#Write a Python program to copy the contents of a file to another file
with open('C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6\\file_handling\\text.txt', 'rt') as x, open('C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6\\file_handling\\\\copy_content_text.txt', 'wt') as y:
    copy = x.read()
    y.write(copy)