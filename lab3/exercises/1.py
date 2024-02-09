#Define a class which has at least two methods: getString: to get a string from console 
#input printString: to print the string in upper case.
class myString:
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
    
    
x = myString()
x.getString()
x.printString()