import math

N = 3
middle = (N*3)+2

## Row 1
print(" " * (middle-1), end="")
print("y", end="")
print(" " * (middle-1),end="\n\n")

## Row 2
print(" " * (middle-1), end="")
print("^", end="")
print(" " * (middle-1),end="\n")

for row in range(0,(N*2)+1,1):
    if (N-row) == 0: # prints vertical middle
        print("-"*((N*6)+3),end="")
        print("> x", end="\n")
        for xlabel in range((N*(-1)),0, 1):
            print(xlabel,"", end="")
        print(" |  ",end="")
        for xlabel in range(1,N+1,1):
            print(xlabel," ", end="")


    else:
        print(" " * (middle-1), end="")
        print("|",(N-row), end="\n")
        print(" " * (middle-2),"|", end="")


    print("", end="\n")
