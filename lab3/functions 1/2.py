#Read in a Fahrenheit temperature. 
#Calculate and display the equivalent centigrade temperature.
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def CCC(frt):
    
    CCC = (5/9) * (frt - 32)
    print(CCC)
    
frt = int(input())

CCC(frt)    