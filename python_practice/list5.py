list=[2,5,6,8,4,1,9,15,7]
count=0
odd=0

for i in list:
    if(i%2==0 ):
        count+=1
    else:
        odd+=1
    
print(count,odd)