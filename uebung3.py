import math

N = 3
MIDDLE = (N*3)+2
format_row = " " * (MIDDLE-1) + "{middle}" + " " * (MIDDLE-1)


## Row 1
print(format_row.format(middle = "y"))
print()

## Row 2
print(format_row.format(middle = "^"))


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
        print(" " * (MIDDLE-1), end="")
        print("|",(N-row), end="\n")
        print(" " * (MIDDLE-2),"|", end="")


    print()
