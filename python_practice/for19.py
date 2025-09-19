


for n in range(1,50):
    count=0

    for i in range(1,n):
        if(n%i==0):
            count+=1
                
    if(count==1):
        print(n,"is the prime number b/w 1 & 50.") 

    