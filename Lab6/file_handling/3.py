#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.
import os

def test_path(path):
    # Check if path exists
    if os.path.exists(path):
        print("The path exists.")
        
        # Find the filename and directory portion
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("The path does not exist.")

path = 'C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6' #my folder
test_path(path)
