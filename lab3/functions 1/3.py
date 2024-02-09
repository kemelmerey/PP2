#Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numlegs, numheads):
    for i in range(1, numheads+1):
        if (i*4)+(numheads-i)*2 == numlegs:
            ans=f"{i} rabbits,{numheads-i} chickens"
            return ans
print("Enter number of legs:")
numlegs=int(input())
print("Enter number of heads")
numheads=int(input())
print(solve(numlegs,numheads))