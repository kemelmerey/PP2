#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
#For example, histogram([4, 9, 7]) should print the following:
#output:
# **** ********* *******
def histogram(items):
    for n in items:
        output = ''  
        times = n    
        
        while times > 0:
            output += '*'
            times = times - 1 
        
        print(output)
# Example
histogram([4, 9, 7])
#output
# ****
# *********
# *******