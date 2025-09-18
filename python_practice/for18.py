for n in range(1,1000):

    c=0
    t=n
    total=0
    a=n


    while(t):
        t=t//10
        c+=1
    # print(c) 

    while(n):
        r=n%10
        p=1
        for i in range(c):
            p=p*r
        # print(p)
        n=n//10
        total+=p

    if(total==a):
        print(a,"Number is Armstrong") 
    
        
        

