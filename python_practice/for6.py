for i in range(10):
    for j in range(10):
        if((j>=2 and j<=7 and i>=2 and i<=7 ) or (i==0 and j==9) or (i==9 and j==9)):
            print(" ",end="  ")
        else:
            print("*",end="  ")
    print()

for i in range(10):
    for j in range(10):
        if((j>=2 and j<=7 and i>=2 and i<=7 ) or i==0 and j==9 or (i==9 and j==9)):
            print(" ",end="  ")
        else:
            print("*",end="  ")
    print()    