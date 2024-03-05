#Write a Python program to delete file by specified path. 
#Before deleting check for access and whether a given path exists or not.
import os
if os.path.exists("C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6\\file_handling\\dir.txt"):
  os.remove("C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6\\file_handling\\dir.txt")
else:
  print("The file does not exist")