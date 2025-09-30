def prime(n):

    count=0
    for i in range(1,n):
        if(n%i==0):
            count+=1
        
        
    if(count==1):
        return n
    return 0


for i in range(1,16):

    p = prime(i)
    if( p!=0 ):
        # print(p)
        for j in range(i+1,16):
            p2 = prime(j)
            if( p2 !=0):
                if(p +p2 == 16):
                    print(p," + ", p2," = ", 16)


        
