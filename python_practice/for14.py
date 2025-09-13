sum=0
n=int(input("Enter number of terms:"))
for i in range(1,n):
    print("+1/",i,end=" ")      
    sum=sum+1/i
print()    
print(sum)    
