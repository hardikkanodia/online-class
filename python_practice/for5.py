for i  in range(9):
    for j in range(10,i,-1):
        print(" ",end=" ")

    for j in range(3):
        print("-",end=" ")
   

    for j in range(0 ,i,1):
        if(i==4 or i==5):
           print("-",end="   ")
        else:
            print(" ",end="   ")

    for j in range(3):
        print("-",end=" ")
    print()
    
    


    