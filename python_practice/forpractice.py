n=47
count=0

for i in range(1,n+1):
    if(n%i==0):
        count+=1
        print(i)  

if(count==2):
    print(n,"is Prime Number.")  
else:
    print(n,"is not prime Number.")          

