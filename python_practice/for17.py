for n in range(1,1000):
    total=0
    for i in range(1,n):
        if(n%i==0):
            #print(i,end=" ")    
            total+=i
         
    if(total==n):
        print("The perfect Number is:",total)        
