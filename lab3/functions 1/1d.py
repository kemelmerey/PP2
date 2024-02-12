#Create a python file and import some of the functions from the above 13 tasks and try to use them.

from 1b import vol
def main():
    radius = float(input("Enter the radius of the cylinder: "))
    volume = vol(radius)
    print("The volume of the cylinder is: ", volume)
if __name__ == "__main__":
    main()