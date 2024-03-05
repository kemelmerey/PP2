#Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path

import os

def check_path_access(path):
    # Check existence
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    # Check readability
    if not os.access(path, os.R_OK):
        print("No read access to the specified path.")
    else:
        print("Read access to the specified path.")
    
    # Check writability
    if not os.access(path, os.W_OK):
        print("No write access to the specified path.")
    else:
        print("Write access to the specified path.")
    
    # Check executability
    if not os.access(path, os.X_OK):
        print("No execute access to the specified path.")
    else:
        print("Execute access to the specified path.")

# Specify the path  to check access for
path = 'C:\\Users\\Admin\\Desktop\\PP2_2024\\Lab6' #my folder 

check_path_access(path)
